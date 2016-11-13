import re

all_professions_list = ['accountant',
 'activist',
 'actor',
 'alchemist',
 'american football player',
 'animator',
 'announcer',
 'anthropologist',
 'architect',
 'art critic',
 'art director',
 'artist',
 'astrologer',
 'astronaut',
 'athlete',
 'attorneys in the united states',
 'audio engineer',
 'author',
 'bandleader',
 'barrister',
 'baseball manager',
 'baseball player',
 'basketball player',
 'bassist',
 'biologist',
 'bishop',
 'bodybuilder',
 'book editor',
 'botanist',
 'broadcaster',
 'bureaucrat',
 'businessperson',
 'cantor',
 'carpenter',
 'cartoonist',
 'choreographer',
 'choreography',
 'cinematographer',
 'civil servant',
 'coach',
 'comedian',
 'commentator',
 'composer',
 'conductor',
 'conservationist',
 'consultant',
 'costume designer',
 'critic',
 'curator',
 'dancer',
 'diplomat',
 'disc jockey',
 'drummer',
 'economist',
 'editor',
 'educator',
 'electrical engineer',
 'electronic musician',
 'engineer',
 'entertainer',
 'entrepreneur',
 'essayist',
 'evangelist',
 'explorer',
 'farmer',
 'fashion designer',
 'fashion model',
 'fighter pilot',
 'film art director',
 'film critic',
 'film director',
 'film editor',
 'film producer',
 'film score composer',
 'financial adviser',
 'fisherman',
 'football player',
 'footballer',
 'friar',
 'game show host',
 'guitarist',
 'harpsichordist',
 'historian',
 'humorist',
 'ice hockey player',
 'illustrator',
 'impresario',
 'insurance broker',
 'inventor',
 'investor',
 'jazz composer',
 'jazz pianist',
 'journalist',
 'judge',
 'keyboard player',
 'law professor',
 'lawyer',
 'legislator',
 'librarian',
 'librettist',
 'lifeguard',
 'lyricist',
 'manager',
 'mathematician',
 'media proprietor',
 'merchant',
 'meteorologist',
 'military aviator',
 'military officer',
 'missionary',
 'model',
 'multi-instrumentalist',
 'music arranger',
 'music artist',
 'music director',
 'musician',
 'music producer',
 'neurologist',
 'novelist',
 'orator',
 'orchestrator',
 'organist',
 'pastor',
 'peace activist',
 'performance artist',
 'philanthropist',
 'philosopher',
 'photographer',
 'physician',
 'physicist',
 'pianist',
 'pilot',
 'pin-up girl',
 'playback singer',
 'playwright',
 'poet',
 'police officer',
 'political activist',
 'politician',
 'polymath',
 'pornographic actor',
 'preacher',
 'presenter',
 'priest',
 'production designer',
 'professor',
 'prophet',
 'psychiatrist',
 'psychoanalyst',
 'psychologist',
 'public speaker',
 'publisher',
 'rabbi',
 'racing driver',
 'radio personality',
 'radio producer',
 'rapper',
 'record producer',
 'revolutionary',
 'rodeo clown',
 'rodeo performer',
 'roman emperor',
 'sailor',
 'scenic designer',
 'science writer',
 'scientist',
 'screenwriter',
 'showgirl',
 'singer',
 'singer-songwriter',
 'soccer player',
 'social activist',
 'soldier',
 'songwriter',
 'sound sculptor',
 'speechwriter',
 'spokesperson',
 'statesman',
 'surveyor',
 'swimmer',
 'talk show host',
 'teacher',
 'television director',
 'television presenter',
 'television producer',
 'television show host',
 'tennis player',
 'tentmaker',
 'theatre director',
 'theatrical producer',
 'theologian',
 'theoretical physicist',
 'tutor',
 'tv editor',
 'tv personality',
 'urban planner',
 'violinist',
 'violist',
 'voice actor',
 'warrior',
 'writer']

profession_synonyms_map = {'accountant':'analyst;clerk;auditor;bookkeeper;comptroller;examiner;calculator;cashier;actuary;cpa;reckoner;teller',
'activist':'revolutionary;advocate;opponent',
'actor':'star;artist;character;clown;player;villain;comedian;entertainer;thespian;impersonator;amateur;ham;lead;extra;understudy;mimic;foil;mime;idol;stooge;bit player;ingenue;performer;trouper;stand-in;walk-on;play-actor;pantomimist;ventriloquist;headliner;barnstormer;soubrette;hambone;ingénue;straight person;thesp',
'alchemist':'warlock;diviner;seer;enchanter;charmer;shaman;conjurer;medium;witch;soothsayer;sorceress;clairvoyant;magician;fortune-teller;occultist;necromancer;thaumaturge;augurer',
'american football player':'',
'animator':'illustrator;artisan;craftsman;landscapist;miniaturist;dauber',
'announcer':'disc jockey;reporter;newscaster;talker;broadcaster;anchorperson;communicator;dj;telecaster;vj;deejay;leader of ceremonies',
'anthropologist':'',
'architect':'designer;artist;builder;creator;planner;engineer;inventor;originator;maker;prime mover;draftsperson;master builder',
'art critic':'craft;profession;dexterity;artistry;knowledge;adroitness;ingenuity;mastery;facility;trade;imagination;know-how;aptitude;expertise;inventiveness;knack;method;virtuosity;craftsmanship',
'art director':'craft;profession;dexterity;artistry;knowledge;adroitness;ingenuity;mastery;facility;trade;imagination;know-how;aptitude;expertise;inventiveness;knack;method;virtuosity;craftsmanship',
'artist':'inventor;artisan;composer;painter;expert;virtuoso;whiz;authority;creator;craftsperson;artiste;handicrafter',
'astrologer':'soothsayer;fortuneteller;prophet;stargazer',
'astronaut':'pilot;cosmonaut',
'athlete':'competitor;player;animal;professional;contestant;sport;jock;jockey;amateur;contender;challenger;shoulders;gorilla;games player;iron person',
'attorneys in the united states':'counsel;mouthpiece;barrister;advocate;lip;proxy;front;counselor;ambulance chaser;pleader;fixer;da',
'audio engineer':'hearing;auditory;audile;aural',
'author':'producer;creator;writer;columnist;journalist;composer;poet;reporter;ghost;originator;playwright;scribe;biographer;scribbler;ghostwriter;wordsmith;essayist;ink slinger',
'bandleader':'composer;conductor;master;teacher',
'barrister':'advocate;counsel;counselor;lawyer;solicitor',
'baseball manager':'',
'baseball player':'',
'basketball player':'ball;hoops',
'bassist':'',
'biologist':'environmentalist;conservationist;zoologist;ecologist;botanist;preservationist',
'bishop':'administrator;pontiff;pope;cleric;patriarch;director;priest;prelate;angel;metropolitan;primate;cap;coadjutor;overseer;diocesan;suffragan;archer;mitre;miter;berretta;abba',
'bodybuilder':'',
'book editor':'essay;album;novel;publication;dictionary;pamphlet;text;work;manual;textbook;fiction;volume;edition;magazine;booklet;brochure;writing;copy;tome;lexicon;periodical;portfolio;primer;dissertation;opus;handbook;reader;roll;thesaurus;tract;compendium;bible;treatise;omnibus;leaflet;encyclopedia;scroll;monograph;paperback;hardcover;nonfiction;speller;folio;codex;atlas;quarto;reprint;octavo;offprint;bestseller;opuscule;preprint;softcover;vade mecum',
'botanist':'environmentalist;conservationist;zoologist;ecologist;biologist;preservationist',
'broadcaster':'disc jockey;reporter;newscaster;talker;anchorperson;communicator;dj;telecaster',
'bureaucrat':'administrator;civil servant;politician;public servant;functionary;desk-jockey',
'businessperson':'merchant;merchandiser;tycoon;capitalist;trafficker;storekeeper;executive;employer;financier;manager;industrialist;suit;operator;entrepreneur;dealer;baron;big wheel;wheeler-dealer;small potatoes;businesswoman;businessman;big-time operator;career person;franchiser',
'cantor':'singer;leader;precentor;hazan;soloist;chanter;vocalist',
'carpenter':'laborer;builder;worker;artisan;chips;craftsperson;woodworker;cabinetmaker;carps;joiner;mason',
'cartoonist':'illustrator;artist;caricaturist;gagster',
'choreographer':'',
'choreography':'dance',
'cinematographer':'',
'civil servant':'local;governmental;domestic;national;civilian;home',
'coach':'trainer;teacher;mentor;tutor;skipper;educator',
'comedian':'entertainer;comic;humorist;clown;actor;stooge;wag;jester;jokester;joker;wit;zany;laugh;card;droll;top banana;farceur;quipster;banana;cutup;merry-andrew;million laughs;stand-up comic;wisecracker',
'commentator':'correspondent;observer;pundit;announcer;writer;critic;reviewer;analyst;interpreter;sportscaster;expositor;annotator',
'composer':'writer;songster',
'conductor':'director;maestro;manager;supervisor;master;marshal;guide',
'conservationist':'environmentalist;guardian;green;tree hugger;preservationist',
'consultant':'specialist;veteran;expert;advisor;counsel;pro;authority;maven;master;mentor;guide;freelancer',
'costume designer':'style;fashion;attire;garb;uniform;apparel;suit;wardrobe;dress;ensemble;getup;mode;guise;rig;duds;outfit;clothing;robes;livery',
'critic':'pundit;expert;cartoonist;authority;judge;reviewer;commentator;connoisseur;sharpshooter;arbiter;diagnostic;expositor;caricaturist;annotator;analyzer;evaluator',
'curator':'director;custodian;administrator;manager;conservator;keeper;guardian;steward',
'dancer':'ballet dancer;danseuse;danseur;hoofer;chorus girl;prima ballerina',
'diplomat':'expert;mediator;envoy;agent;negotiator;representative;minister;ambassador;go-between;emissary;plenipotentiary;moderator;legate;conciliator;tactician',
'disc jockey':'sphere;ring;perimeter;revolution;globe;circus;crown;amphitheater;disk;enclosure;belt;tire;record;bowl;periphery;stadium;hoop;wheel;wreath;horizon;circlet;band;aureole;compass;coil;lap;halo;cycle;circumference;ringlet;bracelet;orbit;corona;meridian;turn;vortex;circuit;round;equator;cirque;cordon;ecliptic;zodiac;colure;full turn;parallel of latitude',
'drummer': '',
'economist':  '',
'editor':'proofreader;copyreader;newspaperwoman;copyholder;newspaperman;rewriter;reviser;deskman;blue-penciler',
'educator':'lecturer;professor;instructor;trainer;coach;dean;monitor;tutor;mentor;schoolteacher;educationist;department head',
'electrical engineer': '',
'electronic musician':'computerized;anodic',
'engineer':'designer;builder;director;surveyor;manager;planner;architect;inventor;originator;schemer;manipulator;techie;sights;contriver;deviser;technie',
'entertainer':'artist;player',
'entrepreneur':'manager;executive;administrator;producer;contractor;undertaker;founder;backer;businessperson;promoter;industrialist;organizer',
'essayist':'producer;creator;writer;columnist;journalist;composer;poet;reporter;ghost;originator;playwright;scribe;biographer;scribbler;ghostwriter;wordsmith;ink slinger;prose writer',
'evangelist':'pastor;missionary;minister;televangelist;revivalist;tv evangelist',
'explorer':'pilgrim;adventurer;pioneer;seeker;traveler;searcher;pathfinder;experimenter;inquisitive person',
'farmer':'rancher;peasant;laborer;producer;grower;tender;reaper;gardener;agriculturist;clodhopper;hired hand;horticulturist;villein;homesteader;gleaner;feeder;planter;agriculturalist;cropper;sower;sharecropper;tiller;agronomist;harvester;cultivator;plower;cob;breeder;country person;grazer',
'fashion designer':'tone;look;form;trend;pattern;thing;shape;mode;model;fad;chic;cut;figure;rage;make;cry;appearance;custom;convention;usage;furor;line;configuration;mold;latest;craze;vogue;dernier cri;last word;latest thing;bandwagon;cultism;cultus;faddism;in thing;newest wrinkle',
'fashion model':'tone;look;form;trend;pattern;thing;shape;mode;model;fad;chic;cut;figure;rage;make;cry;appearance;custom;convention;usage;furor;line;configuration;mold;latest;craze;vogue;dernier cri;last word;latest thing;bandwagon;cultism;cultus;faddism;in thing;newest wrinkle',
'fighter pilot':'warrior;champion;mercenary;assailant;militant;soldier;boxer;combatant;opponent;heavy;competitor;bully;rival;belligerent;contender;pugilist;aggressor;antagonist;contestant;gladiator;wildcat;tanker;warlord;gi;bruiser;brawler;scrapper;battler;disputant;slugger;duelist;punching bag;jouster;person-at-arms;serviceperson',
'film art director':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'film critic':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'film director':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'film editor':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'film producer':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'film score composer':'layer;fold;skin;integument;cloud;web;sheet;fabric;dusting;haze;membrane;opacity;blur;foil;leaf;veil;covering;coat;partition;nebula;transparency;scum;brume;gauze;mistiness;pellicle;haziness;obscuration',
'financial adviser':'fiscal;economic;commercial;monetary;banking;business',
'fisherman':'trawler;fisher;lobsterman;troller',
'football player':'soccer;rugby',
'footballer':'',
'friar':'priest;abbot;solitary;cenobite;recluse;brother;ascetic;religious;monastic;hermit;eremite;anchorite',
'game show host':'gallant;dogged;bold;hardy;inclined;disposed;prepared;spirited;eager;interested;ready;persevering;heroic;courageous',
'guitarist':'',
'harpsichordist':'',
'historian':'professor;writer;teacher;chronicler;historiographer;annalist',
'humorist':'entertainer;clown;jester;joker;wit;comic;jokester;card;satirist;comedienne;cutup;jokesmith',
'ice hockey player':'chunk;glaze;hail;crystal;iceberg;icicle;glacier;sleet;diamonds;hailstone;permafrost;floe',
'illustrator':'cartoonist',
'impresario':'director;sponsor',
'insurance broker':'allowance;coverage;guarantee;warranty;backing;warrant;support;indemnification;cover;indemnity;safeguard;provision;assurance',
'inventor':'designer;founder;author;builder;creator;architect;maker;innovator;originator;pioneer;father;experimenter;coiner',
'investor':'lender;shareholder;banker;backer;capitalist;stockholder;venture capitalist',
'jazz composer':'bop;swing;blues;boogie;boogie-woogie;ragtime;dixieland;jive;bebop',
'jazz pianist':'bop;swing;blues;boogie;boogie-woogie;ragtime;dixieland;jive;bebop',
'journalist':'correspondent;reporter;writer;columnist;press;commentator;announcer;publicist;cub;hack;contributor;scribe;pencil pusher;editor;broadcaster;scrivener;newsperson;stringer',
'judge':'referee;court;expert;justice;authority;critic;inspector;umpire;moderator;negotiator;peacemaker;interpreter;bench;intermediary;intercessor;judiciary;arbiter;warden;magistrate;honor;marshal;adjudicator;assessor;conciliator;chancellor;evaluator;reconciler;appraiser;ombudsman;justice of peace;legal official;magister',
'keyboard player':'manual;piano;console;clavier;ivories;blacks and whites',
'law professor':'case;statute;requirement;code;constitution;charter;mandate;decision;act;legislation;decree;precedent;regulation;ruling;charge;measure;order;covenant;enactment;injunction;canon;summons;precept;behest;dictate;ordinance;prescript;commandment;equity;command;warrant;edict;notice;garnishment;bidding;demand;prescription;institute;instruction;assize;divestiture;writ;subpoena;caveat;jurisprudence;bylaw;decretum;due process;reg',
'lawyer':'counselor;advocate;proctor;attorney;practitioner;barrister;mouthpiece;counsel;solicitor;defender;jurist;jurisprudent;procurator;counsellor;pleader',
'legislator':'administrator;deputy;lawmaker;member;representative;senator;leader;parliamentarian;council member;lawgiver;aldermember;assemblymember',
'librarian':'curator;cataloger',
'librettist':'author;writer;dramatist;scenarist;tragedian;dramaturge',
'lifeguard':'',
'lyricist':'poet;musician;composer;songwriter;lyrist;music writer',
'manager':'administrator;official;supervisor;producer;executive;boss;director;officer;superintendent;organizer;head;comptroller;conductor;exec;governor;proprietor;overseer;straw boss;controller;handler;head person;slavedriver;zookeeper',
'mathematician':'',
'media proprietor':'news;television;radio;correspondence;disclosure;cable;announcement;intelligence;communications;expression;publishing;announcing',
'merchant':'shopkeeper;trafficker;vendor;trader;broker;seller;operator;shipper;dealer;tycoon;businessperson;storekeeper;salesperson;exporter;retailer;wholesaler;sender;handler;jobber;consigner;marketer;tradesperson',
'meteorologist':'witch;seer;prognosticator;prophesier;diviner;medium;sibyl;astrologer;forecaster;reader;wizard;bard;fortuneteller;soothsayer;oracle;augur;auspex;magus;clairvoyant;sorcerer;ovate;palmist;druid;predictor',
'military aviator':'army;fighting;militant;martial;combatant;aggressive;armed;combative;warlike;militaristic;soldierly;warmongering',
'military officer':'army;fighting;militant;martial;combatant;aggressive;armed;combative;warlike;militaristic;soldierly;warmongering',
'missionary':'evangelist;pastor;preacher;messenger;clergy;teacher;apostle;missioner;promoter;herald;propagandist;minister;clergyperson;converter;revivalist;proselytizer',
'model':'miniature;exemplary;perfect;dummy;classical;classic;standard;facsimile;imitation;copy;representative;archetypal;commendable;flawless;illustrative',
'multi-instrumentalist':'',
'music arranger':'soul;rap;rock;melody;piece;singing;tune;hymn;modern;classical;song;bop;chamber;jazz;measure;fusion;refrain;air;strain;harmony;swing;acoustic;folk;hard rock;instrumental;popular;opera;ragtime;plainsong;bebop;a cappella;heavy metal;rock and roll',
'music artist':'soul;rap;rock;melody;piece;singing;tune;hymn;modern;classical;song;bop;chamber;jazz;measure;fusion;refrain;air;strain;harmony;swing;acoustic;folk;hard rock;instrumental;popular;opera;ragtime;plainsong;bebop;a cappella;heavy metal;rock and roll',
'music director':'soul;rap;rock;melody;piece;singing;tune;hymn;modern;classical;song;bop;chamber;jazz;measure;fusion;refrain;air;strain;harmony;swing;acoustic;folk;hard rock;instrumental;popular;opera;ragtime;plainsong;bebop;a cappella;heavy metal;rock and roll',
'musician':'conductor;artist;virtuoso;player;composer;entertainer;performer;soloist;instrumentalist;vocalist;artiste;diva',
'music producer':'soul;rap;rock;melody;piece;singing;tune;hymn;modern;classical;song;bop;chamber;jazz;measure;fusion;refrain;air;strain;harmony;swing;acoustic;folk;hard rock;instrumental;popular;opera;ragtime;plainsong;bebop;a cappella;heavy metal;rock and roll',
'neurologist':'',
'novelist':'writer;storyteller;author;fictionist',
'orator':'preacher;lecturer;rhetorician;declaimer;public speaker;sermonizer;lector;reciter;pontificator',
'orchestrator':'instigator;troublemaker;mastermind;chieftain;head;captain;spokesperson;ruler;general;inciter;chief;agitator;commander;skipper;president;boss;brains;head honcho',
'organist':'',
'pastor':'cleric;vicar;preacher;priest;minister;rector;divine;parson;ecclesiastic;shepherd;reverend',
'peace activist':'reconciliation;accord;love;unity;truce;friendship;conciliation;concord;union;amity;treaty;neutrality;cessation;unanimity;order;armistice;pacification;pacifism',
'performance artist':'work;act;achievement;conduct;completion;enforcement;fruition;consummation;administration;attainment;exploit;fulfillment;realization;discharge;execution;feat;doing;pursuance;carrying out',
'philanthropist':'contributor;donor;benefactor;patron;helper;do-gooder;good samaritan;bleeding heart;altruist',
'philosopher':'logician;sage;savant;theorist;sophist;wise person',
'photographer':'paparazzo;photojournalist;shutterbug',
'physician':'specialist;doctor;quack;medic;intern;healer;general practitioner;surgeon;md;doc;bones;sawbones',
'physicist':'analyst;expert;examiner;prober;chemist;tester',
'pianist':'',
'pilot':'flier;navigator;captain;aviator;leader;scout;jockey;dean;conductor;lead;bellwether;director;ace;flyer;guide;eagle;aerialist;coxswain;steerer;aeronaut;doyen/doyenne',
'pin-up girl':'babe;angel;doll;broad;honey;chick;bathing beauty;beauty queen;cover girl;sex kitten;tomato;centerfold;peach;fox;cupcake;bunny;cutie;cutie-pie;dollface;dream girl;dreamboat',
'playback singer':'',
'playwright':'author;writer;dramatist;scenarist;librettist;tragedian',
'poet':'lyricist;writer;dramatist;author;artist;dilettante;rhymer;bard;versifier;maker;poetaster;parodist;lyrist;librettist;odist',
'police officer':'detective;force;law enforcement;man;corps;bluecoat;pig;blue;law;badge;patrolman;bear;heat;bull;cop;bobby;constable;fuzz;gumshoe;copper;constabulary;fed;oink;officers;narc;flatfoot;gendarme;boy scout;county mounty',
'political activist': '',
'politician':'lawmaker;senator;leader;legislator;partisan;boss;speaker;orator;president;chieftain;public servant;officeholder;grandstander;democrat;republican;baby-kisser;congressperson;handshaker',
'polymath':'educated;scientific;studied;scholarly;accomplished;sound;experienced;versed;cultured;lettered;cultivated;grave;studious;well-grounded;well-read;well-rounded;well-educated;grounded;posted;in the know;pansophic;philosophic;professorial',
'pornographic actor':'immoral;lewd;salacious;indecent;sexy',
'preacher':'cleric;evangelist;missionary;clergy;parson;divine;ecclesiastic;minister;clerical;reverend;sermonizer;revivalist',
'presenter':'contributor;benefactor;patron;backer;angel;subscriber;philanthropist;savior;benefactress;santa claus;donator;altruist;almsgiver;bestower;conferrer;grantor;heavy hitter',
'priest':'cleric;father;monk;preacher;elder;rector;vicar;curate;divine;ecclesiastic;pontiff;clergyperson;father confessor;man of god;lama;friar;padre;holy man;man of the cloth',
'production designer':'manufacture;management;construction;manufacturing;bearing;generation;creation;rendering;assembly;giving;presentation;direction;return;protraction;origination;provision;fabrication;prolongation;blossoming;elongation;yielding;preparation;reproduction;making;producing;formulation;staging;lengthening;fructification;authoring;engendering;extention',
'professor':'lecturer;assistant;fellow;tutor;educator;instructor;teacher;principal;pundit;sage;egghead;savant;brain;pedagogue;faculty member;prof;rocket scientist;quant',
'prophet':'witch;seer;prognosticator;prophesier;diviner;medium;sibyl;astrologer;forecaster;reader;wizard;bard;fortuneteller;soothsayer;oracle;augur;auspex;magus;clairvoyant;sorcerer;ovate;palmist;druid;meteorologist;predictor;evocator;haruspex;horoscopist;seeress;tea-leaf reader',
'psychiatrist':'doctor;therapist;psychoanalyst;shrink;psychotherapist;psychologist;clinician;disorders analyst',
'psychoanalyst':'therapist;analyst;shrink;psychotherapist',
'psychologist':'doctor;therapist;psychoanalyst;shrink;psychotherapist;clinician',
'public speaker':'urban;mutual;civic;civil;national;communal;governmental;social;popular;universal;city;metropolitan;government;country;free;state;common;open;accessible;municipal;unrestricted;widespread;conjoint;open-door;federal;conjunct;free to all;intermutual;not private;without charge',
'publisher':  '',
'rabbi':'priest;teacher;master;rabbin',
'racing driver':'hurrying;flying;running;fast;dashing;swift;rushing;speedy;darting;sailing;zooming;whisking;hastening;whizzing;tearing;galloping',
'radio personality':'transmission;receiver;wireless;walkman;telegraphy;radiotelegraphy;telephony;radiotelegraph;marconi;radiotelephone;am-fm;cb',
'radio producer':'transmission;receiver;wireless;walkman;telegraphy;radiotelegraphy;telephony;radiotelegraph;marconi;radiotelephone;am-fm;cb',
'rapper':'',
'record producer':'story;evidence;note;file;testimony;report;document;transcript;history;inscription;manuscript;memorandum;memo;remembrance;archive;witness;memorial;log;script;writing;annals;archives;memoir;trace;journal;diary;legend;chronicle;register;jacket;almanac;monument;directory;entry;minutes;scroll;track record;documentation;transcription;registry;comic book;paper trail;swindle sheet;written material',
'revolutionary':'subversive;radical;insurgent;rebel;rioting;anarchistic',
'rodeo clown':'festival;roundup;exhibition;competition;enclosure',
'rodeo performer':'festival;roundup;exhibition;competition;enclosure',
'roman emperor':'classic;academic;attic;bookish;canonical;humanistic;latin;hellenic;doric;greek;scholastic;ionic;grecian;augustan;homeric',
'sailor':'cadet;marine;pilot;swab;tarpaulin;mate;jack;seafarer;navigator;mariner;salt;pirate;hearty;sea dog;boater;diver;bluejacket;shipmate;tar;windjammer;middy;lascar;able-bodied sailor;circumnavigator;deck hand;midshipman/woman;old salt',
'scenic designer':'panoramic;breathtaking;dramatic;spectacular;grand;impressive',
'science writer':'discipline;information;art;technique;system;learning;skill;education;lore;scholarship;erudition;branch;wisdom;body of knowledge',
'scientist':'analyst;expert;examiner;prober;physicist;chemist;tester;lab technician',
'screenwriter':'correspondent;author;reporter;critic;columnist;poet;novelist;dramatist;journalist;contributor;scribe;editor;biographer;essayist;wordsmith;scribbler;stenographer;ghostwriter;freelancer;stringer;newspaper person;person of letters;scripter',
'showgirl':  '',
'singer':'artist;musician;voice;troubadour;songbird;songster;minstrel;diva;soloist;crooner;vocalist;artiste;warbler;chorister;accompanist;chanter;nightingale;chanteuse',
'singer-songwriter':'writer;songster',
'soccer player':'rugby;american football',
'social activist':'civil;communal;cordial;group;familiar;collective;community;general;common;societal;sociable;nice;amusing;communicative;companionable;convivial',
'soldier':'fighter;mercenary;guerrilla;veteran;guard;officer;volunteer;marine;pilot;warrior;cadet;infantry;recruit;private;gunner;scout;rank;warmonger;paratrooper;trooper;commando;draftee;musketeer;conscript;gi;green beret;airforce member',
'songwriter':'poet;musician;composer;lyrist',
'sound sculptor':'vigorous;sturdy;solid;vibrant;safe;thorough;flawless;sane;stable;robust;intact;firm;entire;right;fit;well;hale;perfect;total;whole',
'speechwriter':'',
'spokesperson':'deputy;delegate;champion;mediator;prophet;mouthpiece;agent;protagonist;mouth;representative;speaker;substitute;talker;stand-in;prolocutor',
'statesman':'lawmaker;politician;legislator',
'surveyor':'mapmaker;cartographer;assessor;measurer',
'swimmer':'',
'talk show host':'lecture;dissertation;homily;exhortation;harangue;descant;recitation;declamation;spiel;discourse;allocution;oration;monologue;epilogue;sermon;disquisition;prelection;screed;peroration;expatiation;chalk talk',
'teacher':'lecturer;supervisor;scholar;assistant;professor;tutor;coach;educator;instructor;trainer;adviser;preceptor;pundit;mentor;pedagogue;teach;disciplinarian;guide;schoolteacher;faculty member;abecedary',
'television director':'tv set;box;station;video;eye;tv;tube;receiver;baby-sitter;boob tube;idiot box;small screen;audio;telly;vid',
'television presenter':'tv set;box;station;video;eye;tv;tube;receiver;baby-sitter;boob tube;idiot box;small screen;audio;telly;vid',
'television producer':'tv set;box;station;video;eye;tv;tube;receiver;baby-sitter;boob tube;idiot box;small screen;audio;telly;vid',
'television show host':'tv set;box;station;video;eye;tv;tube;receiver;baby-sitter;boob tube;idiot box;small screen;audio;telly;vid',
'tennis player':'',
'tentmaker':'',
'theatre director':'troupe;theater;drama;histrionics;dramatics;theatrics;dramaturgy;footlights;histrionism',
'theatrical producer':'exaggerated;melodramatic;showy;comic;thespian;vaudeville;amateur;ham;show;affected;artificial;ceremonious;histrionic;legitimate;mannered;meretricious;schmaltzy;theatric;campy;operatic;hammy;staged',
'theologian':'cleric;clergy;philosopher;scholar;divine;curate;ecclesiastic',
'theoretical physicist':'imaginative;abstract;metaphysical;intellectual;vague;academic;philosophical;logical;analytical;speculative;assumed',
'tutor':'lecturer;educator;instructor;teacher;mentor;coach;preceptor;guardian;governor;grind;teach;guide;prof;private teacher',
'tv editor':'box;baby-sitter;eye;tube;station;video;receiver;tv set;telly;audio;vid',
'tv personality':'box;baby-sitter;eye;tube;station;video;receiver;tv set;telly;audio;vid',
'urban planner':'downtown;civil;metropolitan;civic',
'violinist':'',
'violist':'',
'voice actor':'sound;speech;cry;tone;statement;exclamation;vent;words;song;modulation;articulation;inflection;roar;mutter;delivery;vocalization;shout;call;murmur;intonation;yell;vociferation;utterance;tongue',
'warrior':'soldier;fighter;hero;champion;combatant;conscript;trooper;gi;battler',
'writer':'correspondent;author;reporter;critic;columnist;poet;novelist;dramatist;journalist;contributor;scribe;editor;biographer;essayist;screenwriter;wordsmith;scribbler;stenographer;ghostwriter;freelancer;stringer;newspaper person;person of letters;scripter',
}

def get_similarity_words(profession):
    return re.findall(r"[\w]+", profession.lower())

def get_similar_professions(profession):
    profession_synonyms = profession_synonyms_map.get(profession)

    if not profession_synonyms:
        profession_words = profession.split(' ')
        #the next transformation is relevant only if the
        #profession consist more than one word, e.g. 'electronical engineer'
        if len(profession_words) > 1:
            last_word = profession_words[-1]
            #search for synonyms of the last word
            last_word_synonyms = profession_synonyms_map.get(last_word.strip())
            if not last_word_synonyms:
                return ''
            result=''

            #get the profession, without the last word
            profession_prefix = profession.replace(last_word, '').strip()
            for last_word_synonym in last_word_synonyms.split(';'):
                #add the first part of the word + the newly found synonym
                result+=profession_prefix + ' ' + last_word_synonym + ';'

            return result[:-2]
        return ''
    else:
        return profession_synonyms_map.get(profession)
