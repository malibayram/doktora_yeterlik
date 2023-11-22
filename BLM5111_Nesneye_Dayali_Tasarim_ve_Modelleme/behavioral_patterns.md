### Behavioral Patterns (Davranışsal Kalıplar):

> Nesnelerin arasındaki etkileşimi tanımlayan kalıplardır.

1. **[Iterator Pattern:](#iterator-pattern)** Bir koleksiyonun elemanları üzerinde dolaşmayı sağlayan bir kalıptır.
2. **[Observer Pattern:](#observer-pattern)** Bir nesnenin durumundaki değişiklikleri, diğer nesnelere bildirmeyi sağlayan bir kalıptır.
3. **[Mediator Pattern:](#mediator-pattern)** Nesneler arasındaki iletişimi merkezi bir nesne üzerinden yapan bir kalıptır.
4. **[Memento Pattern:](#memento-pattern)** Bir nesnenin durumunu saklamayı ve daha sonra geri yüklemeyi sağlayan bir kalıptır.
5. **[Chain of Responsibility Pattern:](#chain-of-responsibility-pattern)** Bir isteğin bir dizi nesne tarafından işlenmesini sağlayan bir kalıptır.
6. **[Command Pattern:](#command-pattern)** Bir isteği bir nesneye aktarılmasını ve daha sonra nesne tarafından işlenmesini sağlayan bir kalıptır.
7. **[State Pattern:](#state-pattern)** Bir nesnenin davranışını, durumuna göre değiştiren bir kalıptır.
8. **[Strategy Pattern:](#strategy-pattern)** Bir algoritmayı birden fazla nesne tarafından kullanılmasını sağlayan bir kalıptır.
9. **[Template Method Pattern:](#template-method-pattern)**: Bir algoritmanın iskeletini tanımlayan ve bazı adımların alt sınıflar tarafından uygulanmasını sağlayan bir kalıptır.
10. **[Visitor Pattern:](#visitor-pattern)** Bir nesne yapısında dolaşmayı ve her nesne üzerinde bir işlem yapmayı sağlayan bir kalıptır.

#### Iterator Pattern
 Testt
> Class Diagram:

```mermaid
classDiagram
class SocialSpammer {
    +send(iterator: Iterator, message: String)
}
class Application {
    -networks: List<SocialNetwork>
    +sendSpamToFriends(profileId: String, message: String)
    +sendSpamToCoworkers(profileId: String, message: String)
}
class SocialNetwork {
    +createFriendsIterator(profileId: String)
    +createCoworkersIterator(profileId: String)
}
<<interface>> SocialNetwork
class ProfileIterator {
    +getNext()
    +hasMore()
}
<<interface>> ProfileIterator
class Facebook {
    +createFriendsIterator(profileId: String)
    +createCoworkersIterator(profileId: String)
}
class FacebookIterator {
    -facebook: Facebook
    -profileId: String
    -type: String
    -currentPosition: int
    -cache: List<String>
    +FacebookIterator(facebook: Facebook, profileId: String, type: String)
    +lazyLoad()
    +getNext()
    +hasMore()
}
class Profile {
    -id: String
    -email: String
    +Profile(id: String, email: String)
    +getId()
    +getEmail()
}
SocialSpammer --> ProfileIterator
SocialSpammer ..> Profile
Application --> SocialSpammer
Application --> Facebook
Facebook <--> FacebookIterator
FacebookIterator ..|> ProfileIterator
SocialNetwork ..> ProfileIterator
ProfileIterator ..> Profile
Facebook o--> Profile
```

> Java Code:

```java
public interface ProfileIterator {
    Profile getNext();
    boolean hasMore();
}

public interface SocialNetwork {
    ProfileIterator createFriendsIterator(String profileId);
    ProfileIterator createCoworkersIterator(String profileId);
}

public class Facebook implements SocialNetwork {
    public ProfileIterator createFriendsIterator(String profileId) {
        return new FacebookIterator(this, profileId, "friends");
    }
    public ProfileIterator createCoworkersIterator(String profileId) {
        return new FacebookIterator(this, profileId, "coworkers");
    }
}

public class FacebookIterator implements ProfileIterator {
    private Facebook facebook;
    private String profileId;
    private String type;
    private int currentPosition = 0;
    private List<String> cache;
    public FacebookIterator(Facebook facebook, String profileId, String type) {
        this.facebook = facebook;
        this.profileId = profileId;
        this.type = type;
    }
    private void lazyLoad() {
        if (cache == null) {
            cache = facebook.requestProfileFriendsFromFacebook(profileId, type);
        }
    }
    @Override
    public Profile getNext() {
        if (!hasMore()) {
            return null;
        }
        String friendId = cache.get(currentPosition);
        Profile friendProfile = facebook.requestProfileFromFacebook(friendId);
        currentPosition++;
        return friendProfile;
    }
    @Override
    public boolean hasMore() {
        lazyLoad();
        return currentPosition < cache.size();
    }
}

public class Profile {
    private String id;
    private String email;

    public Profile(String id, String email) {
        this.id = id;
        this.email = email;
    }

    public String getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }
}

public class SocialSpammer {
    public void send(ProfileIterator iterator, String message) {
        while (iterator.hasMore()) {
            Profile profile = iterator.getNext();
            System.out.println("Sending message to " + profile.getEmail() + ": " + message);
        }
    }
}

```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Observer Pattern

> Class Diagram:

```mermaid
classDiagram
class EventListeners {
    +update(filename: String)
}
<<interface>> EventListeners
class EventManager {
    -listeners: ~Map~
    +subscribe(eventType: String, listener: EventListeners)
    +unsubscribe(eventType: String, listener: EventListeners)
    +notify(eventType: String, filename: String)
}
class Editor {
    -events: EventManager
    -filename: String
    +openFile(filename: String)
    +saveFile()
}
class EmailAlertListener {
    -email: String
    +update(filename: String)
}
class LoggingListener {
    -log: String
    +update(filename: String)
}
EventListeners <|.. EmailAlertListener
EventListeners <|.. LoggingListener
Editor o--> EventManager
EventManager o--> EventListeners
```

> Java Code:

```java
public interface EventListeners {
    void update(String filename);
}

public class EventManager {
    Map<String, List<EventListeners>> listeners = new HashMap<>();

    public EventManager(String... operations) {
        for (String operation : operations) {
            this.listeners.put(operation, new ArrayList<>());
        }
    }

    public void subscribe(String eventType, EventListeners listener) {
        List<EventListeners> users = listeners.get(eventType);
        users.add(listener);
    }

    public void unsubscribe(String eventType, EventListeners listener) {
        List<EventListeners> users = listeners.get(eventType);
        users.remove(listener);
    }

    public void notify(String eventType, String filename) {
        List<EventListeners> users = listeners.get(eventType);
        for (EventListeners listener : users) {
            listener.update(filename);
        }
    }
}

public class Editor {
    public EventManager events;
    private String filename;

    public Editor() {
        this.events = new EventManager("open", "save");
    }

    public void openFile(String filename) {
        this.filename = filename;
        events.notify("open", filename);
    }

    public void saveFile() throws Exception {
        if (this.filename != null) {
            events.notify("save", filename);
        } else {
            throw new Exception("Please open a file first.");
        }
    }
}

public class EmailAlertListener implements EventListeners {
    private String email;

    public EmailAlertListener(String email) {
        this.email = email;
    }

    @Override
    public void update(String filename) {
        System.out.println("Email to " + email + ": Someone has performed " + filename + " operation with the following file: " + filename);
    }
}

public class LoggingListener implements EventListeners {
    private String log;

    public LoggingListener(String filename) {
        this.log = filename;
    }

    @Override
    public void update(String filename) {
        System.out.println("Logging to file: Someone has performed " + filename + " operation with the following file: " + filename);
    }
}

public class Demo {
    public static void main(String[] args) {
        Editor editor = new Editor();
        EventListeners emailAlertsListener = new EmailAlertListener("email@emial.com");
        EventListeners loggingListener = new LoggingListener("/path/to/log/file.txt");
        editor.events.subscribe("open", emailAlertsListener);
        editor.events.subscribe("save", emailAlertsListener);
        editor.events.subscribe("save", loggingListener);
        try {
            editor.openFile("test.txt");
            editor.saveFile();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Mediator Pattern

> Class Diagram:

```mermaid
classDiagram
class Mediator {
    +notify(sender: Component, event: String)
}
<<interface>> Mediator
class AuthenticationDialog {
    -title: Title
    -loginOrRegister: TextBox
    -login, password: TextBox
    -rememberMe: CheckBox
    -ok, cancel: Button
    +notify(sender: Component, event: String)
}
class Component {
    -dialog: Mediator
    +click()
    +keypress()
    +change()
    +updateUI()
}
<<abstract>> Component
class CheckBox {
    ...
    +check()
}
Button --|> Component
TextBox --|> Component
CheckBox --|> Component
Button <--* AuthenticationDialog
TextBox <--* AuthenticationDialog
CheckBox <--* AuthenticationDialog
Mediator <--> Component
Mediator <|-- AuthenticationDialog
```

> Java Code:

```java

public interface Mediator {
    void notify(Component sender, String event);
}

public class AuthenticationDialog implements Mediator {
    private Title title;
    private TextBox loginOrRegister;
    private TextBox login;
    private TextBox password;
    private CheckBox rememberMe;
    private Button ok;
    private Button cancel;

    @Override
    public void notify(Component sender, String event) {
        if (sender == loginOrRegister && event == "click") {
            title.setText("Log in");
            loginOrRegister.hide();
            // ...
        }
        if (sender == rememberMe && event == "check") {
            // ...
        }
        // ...
    }
}

public class Component {
    protected Mediator dialog;

    public Component(Mediator dialog) {
        this.dialog = dialog;
    }

    public void click() {
        dialog.notify(this, "click");
    }

    public void keypress() {
        dialog.notify(this, "keypress");
    }

    public void change() {
        dialog.notify(this, "change");
    }

    public abstract void updateUI();
}

public class Button extends Component {
    public Button(Mediator dialog) {
        super(dialog);
    }

    public void click() {
        dialog.notify(this, "click");
    }

    @Override
    public void updateUI() {
        // ...
    }
}

public class TextBox extends Component {
    public TextBox(Mediator dialog) {
        super(dialog);
    }

    @Override
    public void updateUI() {
        // ...
    }

    public void setText(String text) {
        // ...
    }

    public String getText() {
        // ...
    }
}

public class CheckBox extends Component {
    public CheckBox(Mediator dialog) {
        super(dialog);
    }

    @Override
    public void updateUI() {
        // ...
    }

    public boolean isChecked() {
        // ...
    }

    public void setChecked(boolean checked) {
        // ...
    }
}

public class Demo {
    public static void main(String[] args) {
        AuthenticationDialog authenticationDialog = new AuthenticationDialog();
        authenticationDialog.click();
        authenticationDialog.click();
    }
}

```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Memento Pattern

> Class Diagram:

```mermaid
classDiagram
class Editor {
    -state
    +setState(x)
    +createSnapshot()
}
class Snapshot {
    -state
    +Snapshot(state)
    +restore()
}
class Command {
    -backup: Snapshot
    +makeBackup()
    +undo()
}
Snapshot <-- Command
Editor <--> Snapshot
```

> Java Code:

```java
public class Editor {
    private String state;

    public void setState(String state) {
        this.state = state;
    }

    public Snapshot createSnapshot() {
        return new Snapshot(state);
    }

    public void restoreSnapshot(Snapshot snapshot) {
        this.state = snapshot.getState();
    }
}

public class Snapshot {
    private String state;

    public Snapshot(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

public class Command {
    private Editor editor;
    private Snapshot backup;

    public Command(Editor editor) {
        this.editor = editor;
    }

    public void makeBackup() {
        backup = editor.createSnapshot();
    }

    public void undo() {
        editor.restoreSnapshot(backup);
    }
}

public class Demo {
    public static void main(String[] args) {
        Editor editor = new Editor();
        Command command = new Command(editor);
        editor.setState("a");
        command.makeBackup();
        editor.setState("b");
        editor.setState("c");
        command.undo();
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Chain of Responsibility Pattern

> Class Diagram:

```mermaid
classDiagram
class ComponentWithContextualHelp {
    +showHelp()
}
<<interface>> ComponentWithContextualHelp
class Component {
    -container: Container
    +tooltipText: String
    +showHelp()
}
class Container {
    -children: List<Component>
    +add(child: Component)
}
class Panel {
    -modalHelpText: String
    +showHelp()
}
class Dialog {
    -wikiPageURL: String
    +showHelp()
}

ComponentWithContextualHelp <|.. Component
Button --|> Component
Container --|> Component
Panel --|> Container
Dialog --|> Container
Component <--o Container
Container --> Component

note for Button "inherit showHelp() from the parent class"
note for Component "if (tooltipText != null) {
        // show tooltip...
    } else {
        // .. or ask the container
        // to do it
        container.showHelp()
    }"
note for Panel "if (modalHelpText != null) {
        // show modal window
        // with a help text
    } else {
        parent::showHelp()
}"
note for Dialog "if (wikiPageURL != null) {
        // open wiki help page
    } else {
        parent::showHelp()
}"
```

> Java Code:

```java
public interface ComponentWithContextualHelp {
    void showHelp();
}

public class Component {
    protected Container container;
    protected String tooltipText;

    public Component(Container container) {
        this.container = container;
    }

    public void showHelp() {
        if (tooltipText != null) {
            // show tooltip...
        } else {
            // .. or ask the container
            // to do it
            container.showHelp();
        }
    }
}

public class Container {
    protected List<Component> children = new ArrayList<>();

    public void add(Component child) {
        children.add(child);
        child.container = this;
    }

    public void showHelp() {
        if (parent != null) {
            super.showHelp();
        }
    }
}

public class Panel extends Container {
    protected String modalHelpText;

    public void showHelp() {
        if (modalHelpText != null) {
            // show modal window
            // with a help text
        } else {
            super.showHelp();
        }
    }
}

public class Dialog extends Container {
    protected String wikiPageURL;

    public void showHelp() {
        if (wikiPageURL != null) {
            // open wiki help page
        } else {
            super.showHelp();
        }
    }
}

public class Demo {
    public static void main(String[] args) {
        Dialog dialog = new Dialog();
        Panel panel = new Panel();
        Button button = new Button();
        dialog.add(panel);
        panel.add(button);
        button.showHelp();
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Command Pattern

> Class Diagram:

```mermaid
classDiagram
class Application {
    -clipboard: String
    -editor: Editor
    -history: List<Command>
    +executeCommand(command: Command)
    +undo()
    +getClipboard()
}
class Editor {
    -text: String
    +deleteSelection()
    +replaceSelection(text: String)
    +getSelection()
}
class Command {
    -app: Application
    -editor: Editor
    -backup: String
    +saveBackup()
    +undo()
    +execute()*
}
<<interface>> Command
class CopyCommand {
    +execute()
}
class CutCommand {
    +execute()
}
class PasteCommand {
    +execute()
}
class UndoCommand {
    +execute()
}
Application o--> Editor
Application o--> Command
Application --> Command : buttons|shortcuts
Command <|-- CopyCommand
Command <|-- CutCommand
Command <|-- PasteCommand
Command <|-- UndoCommand
CopyCommand --> Editor
CutCommand --> Editor
PasteCommand --> Editor
UndoCommand --> Application
```

> Java Code:

```java

public class Application {
    public String clipboard;
    private Editor editor;
    private List<Command> history = new ArrayList<>();

    public void executeCommand(Command command) {
        if (command.execute()) {
            history.add(command);
        }
    }

    public void undo() {
        if (history.size() > 0) {
            Command command = history.get(history.size() - 1);
            if (command != null) {
                command.undo();
                history.remove(command);
            }
        }
    }

    public String getClipboard() {
        return clipboard;
    }
}

public class Editor {
    public String text;

    public void deleteSelection() {
        text = "";
    }

    public void replaceSelection(String text) {
        this.text = text;
    }

    public String getSelection() {
        return text;
    }
}

public interface Command {
    private Application app;
    private Editor editor;
    private String backup;

    public Command(Application app, Editor editor) {
        this.app = app;
        this.editor = editor;
    }

    public void saveBackup() {
        backup = editor.text;
    }

    public void undo() {
        editor.text = backup;
    }

    void execute();
}

public class CopyCommand implements Command {
    public CopyCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        app.clipboard = editor.getSelection();
    }
}

public class CutCommand implements Command {
    public CutCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        saveBackup();
        app.clipboard = editor.getSelection();
        editor.deleteSelection();
    }
}

public class PasteCommand implements Command {
    public PasteCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        saveBackup();
        editor.replaceSelection(app.clipboard);
    }
}

public class UndoCommand implements Command {
    public UndoCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        app.undo();
    }
}

public class Demo {
    public static void main(String[] args) {
        Editor editor = new Editor();
        Application app = new Application();
        app.copy();
        app.paste();
        app.cut();
        app.undo();
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### State Pattern

> Class Diagram:

```mermaid
classDiagram
class State {
    -player: Player
    +State(player: Player)
    +clickLock()*
    +clickPlay()*
    +clickNext()*
    +clickPrevious()*
}
<<interface>> State
class LockedState {
    +clickLock()
    +clickPlay()
    +clickNext()
    +clickPrevious()
}
class ReadyState {
    +clickLock()
    +clickPlay()
    +clickNext()
    +clickPrevious()
}
class PlayingState {
    +clickLock()
    +clickPlay()
    +clickNext()
    +clickPrevious()
}
class Player {
    -state: State
    -playing: boolean
    -playlist: List<String>
    -currentTrack: int
    +Player()
    +changeState(state: State)
    +getState()
    +setPlaying(playing: boolean)
    +isPlaying()
    +startPlayback()
    +nextTrack()
    +previousTrack()
    +setCurrentTrackAfterStop()
}
State <|-- LockedState
State <|-- ReadyState
State <|-- PlayingState
Player o--> State
```

> Java Code:

```java

public interface State {
    private Player player;

    public State(Player player) {
        this.player = player;
    }

    public abstract String clickLock();
    public abstract String clickPlay();
    public abstract String clickNext();
    public abstract String clickPrevious();
}

public class LockedState implements State {
    public LockedState(Player player) {
        super(player);
        player.setPlaying(false);
    }

    @Override
    public String clickLock() {
        if (player.isPlaying()) {
            player.changeState(new PlayingState(player));
            return "Stop playing";
        } else {
            player.changeState(new ReadyState(player));
            return "Locked...";
        }
    }

    @Override
    public String clickPlay() {
        player.changeState(new ReadyState(player));
        return "Locked...";
    }

    @Override
    public String clickNext() {
        return "Locked...";
    }

    @Override
    public String clickPrevious() {
        return "Locked...";
    }
}

public class ReadyState implements State {
    public ReadyState(Player player) {
        super(player);
    }

    @Override
    public String clickLock() {
        player.changeState(new LockedState(player));
        return "Locked...";
    }

    @Override
    public String clickPlay() {
        String action = player.startPlayback();
        player.changeState(new PlayingState(player));
        return action;
    }

    @Override
    public String clickNext() {
        return "Locked...";
    }

    @Override
    public String clickPrevious() {
        return "Locked...";
    }
}

public class PlayingState implements State {
    public PlayingState(Player player) {
        super(player);
    }

    @Override
    public String clickLock() {
        player.changeState(new LockedState(player));
        player.setCurrentTrackAfterStop();
        return "Stop playing";
    }

    @Override
    public String clickPlay() {
        player.changeState(new ReadyState(player));
        return "Paused...";
    }

    @Override
    public String clickNext() {
        String action = player.nextTrack();
        if (action.equals("Starting first track")) {
            return action;
        }
        return "Playing next track";
    }

    @Override
    public String clickPrevious() {
        String action = player.previousTrack();
        if (action.equals("Starting first track")) {
            return action;
        }
        return "Playing previous track";
    }
}

public class Player {
    private State state;
    private boolean playing = false;
    private List<String> playlist = new ArrayList<>();
    private int currentTrack = 0;

    public Player() {
        this.state = new ReadyState(this);
        setPlaying(true);
        for (int i = 1; i <= 12; i++) {
            playlist.add("Track " + i);
        }
    }

    public void changeState(State state) {
        this.state = state;
    }

    public State getState() {
        return state;
    }

    public void setPlaying(boolean playing) {
        this.playing = playing;
    }

    public boolean isPlaying() {
        return playing;
    }

    public String startPlayback() {
        return "Playing " + playlist.get(currentTrack);
    }

    public String nextTrack() {
        currentTrack++;
        if (currentTrack > playlist.size() - 1) {
            currentTrack = 0;
        }
        return "Playing " + playlist.get(currentTrack);
    }

    public String previousTrack() {
        currentTrack--;
        if (currentTrack < 0) {
            currentTrack = playlist.size() - 1;
        }
        return "Playing " + playlist.get(currentTrack);
    }

    public void setCurrentTrackAfterStop() {
        this.currentTrack = 0;
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Strategy Pattern

> Class Diagram:

```mermaid
classDiagram
class RouteStrategy {
    +buildRoute(a, b)*
}
<<interface>> RouteStrategy
class RoadStrategy {
    +buildRoute(a, b)
}
class PublicTransportStrategy {
    +buildRoute(a, b)
}
class WalkingStrategy {
    +buildRoute(a, b)
}
class Navigator {
    -strategy: RouteStrategy
    +Navigator(strategy: RouteStrategy)
    +buildRoute(a, b)
}
RouteStrategy <|.. RoadStrategy
RouteStrategy <|.. PublicTransportStrategy
RouteStrategy <|.. WalkingStrategy
Navigator o--> RouteStrategy
```

> Java Code:

```java
public interface RouteStrategy {
    public void buildRoute(int a, int b);
}

public class RoadStrategy implements RouteStrategy {
    @Override
    public void buildRoute(int a, int b) {
        System.out.println("RoadStrategy: " + a + " -> " + b);
    }
}

public class PublicTransportStrategy implements RouteStrategy {
    @Override
    public void buildRoute(int a, int b) {
        System.out.println("PublicTransportStrategy: " + a + " -> " + b);
    }
}

public class WalkingStrategy implements RouteStrategy {
    @Override
    public void buildRoute(int a, int b) {
        System.out.println("WalkingStrategy: " + a + " -> " + b);
    }
}

public class Navigator {
    private RouteStrategy strategy;

    public Navigator(RouteStrategy strategy) {
        this.strategy = strategy;
    }

    public void buildRoute(int a, int b) {
        strategy.buildRoute(a, b);
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Template Method Pattern

> Class Diagram:

```mermaid
classDiagram
class GameAI {
    +takeTurn()
    +collectResources()
    +buildStructures()*
    +buildUnits()*
    +attack()
    +sendScouts(position)*
    +sendWarriors(position)*
}
<<abstract>> GameAI
class OrcsAI {
    +buildStructures()
    +buildUnits()
    +sendScouts(position)
    +sendWarriors(position)
}
class MonstersAI {
    +collectResources()
    +buildStructures()
    +buildUnits()
    +sendScouts(position)
    +sendWarriors(position)
}
GameAI <|-- OrcsAI
GameAI <|-- MonstersAI
```

> Java Code:

```java
public abstract class GameAI {
    public void takeTurn() {
        collectResources();
        buildStructures();
        buildUnits();
        attack();
    }

    public abstract void collectResources();
    public abstract void buildStructures();
    public abstract void buildUnits();
    public abstract void attack();
}

public class OrcsAI extends GameAI {
    @Override
    public void collectResources() {
        System.out.println("OrcsAI: Collecting gold...");
    }

    @Override
    public void buildStructures() {
        System.out.println("OrcsAI: Building strong structures...");
    }

    @Override
    public void buildUnits() {
        System.out.println("OrcsAI: Building strong units...");
    }

    @Override
    public void attack() {
        System.out.println("OrcsAI: Attacking enemies...");
    }
}

public class MonstersAI extends GameAI {
    @Override
    public void collectResources() {
        System.out.println("MonstersAI: Collecting gold...");
    }

    @Override
    public void buildStructures() {
        System.out.println("MonstersAI: Building strong structures...");
    }

    @Override
    public void buildUnits() {
        System.out.println("MonstersAI: Building strong units...");
    }

    @Override
    public void attack() {
        System.out.println("MonstersAI: Attacking enemies...");
    }
}

```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)

---

#### Visitor Pattern

```mermaid
classDiagram
class Visitor {
    +visitDot(d: Dot)
    +visitCircle(c: Circle)
}
<<interface>> Visitor
class XMLExportVisitor {
    +export(drawing: Drawing)
    +visitDot(d: Dot)
    +visitCircle(c: Circle)
}
class Shape {
    +move(x, y)
    +draw()
    +accept(visitor: Visitor)
}
<<interface>> Shape
class Dot {
    +x: int
    +y: int
    +accept(visitor: Visitor)
}
class Circle {
    +x: int
    +y: int
    +radius: int
    +accept(visitor: Visitor)
}
Visitor <|.. XMLExportVisitor
Shape <|.. Dot
Shape <|.. Circle
Shape <..> XMLExportVisitor : application
Shape ..> Visitor
Visitor ..> Dot
Visitor ..> Circle
```

> Java Code:

```java
public interface Visitor {
    void visitDot(Dot d);
    void visitCircle(Circle c);
}

public class XMLExportVisitor implements Visitor {
    public String export(Drawing drawing) {
        StringBuilder sb = new StringBuilder();
        sb.append("<?xml version=\"1.0\" encoding=\"utf-8\"?>" + System.lineSeparator());
        sb.append("<drawing>" + System.lineSeparator());
        for (Shape shape : drawing.getShapes()) {
            sb.append(shape.accept(this)).append(System.lineSeparator());
        }
        sb.append("</drawing>" + System.lineSeparator());
        return sb.toString();
    }

    @Override
    public String visitDot(Dot d) {
        return String.format("<dot x=\"%d\" y=\"%d\" />", d.getX(), d.getY());
    }

    @Override
    public String visitCircle(Circle c) {
        return String.format(
                "<circle x=\"%d\" y=\"%d\" radius=\"%d\" />",
                c.getX(), c.getY(), c.getRadius()
        );
    }
}

public interface Shape {
    void move(int x, int y);
    void draw();
    String accept(Visitor visitor);
}

public class Dot implements Shape {
    private int x;
    private int y;

    public Dot(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String accept(Visitor visitor) {
        return visitor.visitDot(this);
    }
}

public class Circle implements Shape {
    private int x;
    private int y;
    private int radius;

    public Circle(int x, int y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public String accept(Visitor visitor) {
        return visitor.visitCircle(this);
    }
}

public class Demo {
    public static void main(String[] args) {
        Drawing drawing = new Drawing();
        drawing.addShape(new Dot(1, 10));
        drawing.addShape(new Circle(10, 20, 30));
        Visitor xmlExportVisitor = new XMLExportVisitor();
        System.out.println(xmlExportVisitor.export(drawing));
    }
}
```

[Go Top](#behavioral-patterns-davranışsal-kalıplar)
