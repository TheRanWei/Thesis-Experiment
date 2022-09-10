/*********************************** 
 * Eating Observation Exp 2.0 Test *
 ***********************************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.0.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Eating Observation Exp 2.0';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Instruction__screenRoutineBegin());
flowScheduler.add(Instruction__screenRoutineEachFrame());
flowScheduler.add(Instruction__screenRoutineEnd());
const Baseline_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Baseline_trialsLoopBegin(Baseline_trialsLoopScheduler));
flowScheduler.add(Baseline_trialsLoopScheduler);
flowScheduler.add(Baseline_trialsLoopEnd);
flowScheduler.add(Begin_Video_obs_taskRoutineBegin());
flowScheduler.add(Begin_Video_obs_taskRoutineEachFrame());
flowScheduler.add(Begin_Video_obs_taskRoutineEnd());
const eo_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(eo_trialsLoopBegin(eo_trialsLoopScheduler));
flowScheduler.add(eo_trialsLoopScheduler);
flowScheduler.add(eo_trialsLoopEnd);
flowScheduler.add(BreakRoutineBegin());
flowScheduler.add(BreakRoutineEachFrame());
flowScheduler.add(BreakRoutineEnd());
flowScheduler.add(RemainderRoutineBegin());
flowScheduler.add(RemainderRoutineEachFrame());
flowScheduler.add(RemainderRoutineEnd());
const fo_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(fo_loopLoopBegin(fo_loopLoopScheduler));
flowScheduler.add(fo_loopLoopScheduler);
flowScheduler.add(fo_loopLoopEnd);
flowScheduler.add(BreakRoutineBegin());
flowScheduler.add(BreakRoutineEachFrame());
flowScheduler.add(BreakRoutineEnd());
flowScheduler.add(RemainderRoutineBegin());
flowScheduler.add(RemainderRoutineEachFrame());
flowScheduler.add(RemainderRoutineEnd());
const nf_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(nf_trialsLoopBegin(nf_trialsLoopScheduler));
flowScheduler.add(nf_trialsLoopScheduler);
flowScheduler.add(nf_trialsLoopEnd);
flowScheduler.add(Thank_youRoutineBegin());
flowScheduler.add(Thank_youRoutineEachFrame());
flowScheduler.add(Thank_youRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.1';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var Instruction__screenClock;
var Instruction;
var begin_exp;
var Baseline_codeClock;
var study_trial;
var Baseline_StroopClock;
var baseline_stroop_word;
var baseline_fixation;
var key_resp;
var Begin_Video_obs_taskClock;
var begin_video_obs;
var proceed_to_conditions;
var EO_CODEClock;
var eo_trial;
var EO_ConditionClock;
var eo_Stroop_word;
var eo_fixation_cross;
var key_resp_2;
var BreakClock;
var Break_text;
var end_break;
var RemainderClock;
var stroop_remainder;
var proceed_to_next_condition;
var FO_CODEClock;
var fo_trial;
var FO_ConditionClock;
var fo_fixation_cross;
var fo_word;
var key_resp_3;
var NF_CODEClock;
var nf_trial;
var NF_ConditionClock;
var nf_fixation_cross;
var nf_word;
var key_resp_4;
var Thank_youClock;
var text;
var end_key;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instruction__screen"
  Instruction__screenClock = new util.Clock();
  Instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruction',
    text: "There are two sections in this part of the experiment:\n\nIn the first section, you will complete some color-naming tasks, in which you will name the color of the word presented in the center of the screen by pressing corresponding keyboard keys :\n\nPress 'd' for red; \nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nIn the second section, you will watch some short video clips. After each video clip, you will complete a color-naming task, which will be similar to what you will do in the first section(Press 'd' for red; press 'f' for green, press 'j' for blue, press 'k' for black).\n\nTo familiarize you with the task, there will be 15 practice trials for the color-naming task at the begining of this section. No video clips will be included in practice trials.\n\nPress the 'right arrow' key if you are ready to proceed.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  begin_exp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Baseline_code"
  Baseline_codeClock = new util.Clock();
  study_trial = 0;
  
  // Initialize components for Routine "Baseline_Stroop"
  Baseline_StroopClock = new util.Clock();
  baseline_stroop_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_stroop_word',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  baseline_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_fixation',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Begin_Video_obs_task"
  Begin_Video_obs_taskClock = new util.Clock();
  begin_video_obs = new visual.TextStim({
    win: psychoJS.window,
    name: 'begin_video_obs',
    text: "next, you will watch some videos and complete the stroop task\n\nPress the 'right arrow' key to proceed.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  proceed_to_conditions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EO_CODE"
  EO_CODEClock = new util.Clock();
  eo_trial = 0;
  console.log(eo_word_lst);
  console.log(eo_color_lst);
  
  // Initialize components for Routine "EO_Condition"
  EO_ConditionClock = new util.Clock();
  eo_Stroop_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'eo_Stroop_word',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  eo_fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'eo_fixation_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Break"
  BreakClock = new util.Clock();
  Break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Break_text',
    text: "Now, you can take a break for up to 10 minutes. The experiment will proceed after 10 minutes, but you can end the break early by pressing 'right arrow' key.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  end_break = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Remainder"
  RemainderClock = new util.Clock();
  stroop_remainder = new visual.TextStim({
    win: psychoJS.window,
    name: 'stroop_remainder',
    text: "Please determine the color of the word presented in the center of the screen after the video by pressing corresponding keyboard keys:\n\nPress 'd' for red,\nPress 'f' for green,\nPress 'j' for blue,\nPress 'k' fpr black\n\nPress the 'right arrow' key to proceed.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  proceed_to_next_condition = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FO_CODE"
  FO_CODEClock = new util.Clock();
  fo_trial = 0;
  console.log(fo_word_lst);
  console.log(fo_color_lst);
  
  // Initialize components for Routine "FO_Condition"
  FO_ConditionClock = new util.Clock();
  fo_fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fo_fixation_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  fo_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'fo_word',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "NF_CODE"
  NF_CODEClock = new util.Clock();
  nf_trial = 0;
  console.log(nf_word_lst);
  console.log(nf_color_lst);
  
  // Initialize components for Routine "NF_Condition"
  NF_ConditionClock = new util.Clock();
  nf_fixation_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'nf_fixation_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  nf_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'nf_word',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Thank_you"
  Thank_youClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'You have completed the experiment!\n\nThank you for your participation!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _begin_exp_allKeys;
var Instruction__screenComponents;
function Instruction__screenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instruction__screen'-------
    t = 0;
    Instruction__screenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    begin_exp.keys = undefined;
    begin_exp.rt = undefined;
    _begin_exp_allKeys = [];
    // keep track of which components have finished
    Instruction__screenComponents = [];
    Instruction__screenComponents.push(Instruction);
    Instruction__screenComponents.push(begin_exp);
    
    for (const thisComponent of Instruction__screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction__screenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instruction__screen'-------
    // get current time
    t = Instruction__screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruction* updates
    if (t >= 0.0 && Instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruction.tStart = t;  // (not accounting for frame time here)
      Instruction.frameNStart = frameN;  // exact frame index
      
      Instruction.setAutoDraw(true);
    }

    
    // *begin_exp* updates
    if (t >= 2 && begin_exp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_exp.tStart = t;  // (not accounting for frame time here)
      begin_exp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { begin_exp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { begin_exp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { begin_exp.clearEvents(); });
    }

    if (begin_exp.status === PsychoJS.Status.STARTED) {
      let theseKeys = begin_exp.getKeys({keyList: ['right'], waitRelease: false});
      _begin_exp_allKeys = _begin_exp_allKeys.concat(theseKeys);
      if (_begin_exp_allKeys.length > 0) {
        begin_exp.keys = _begin_exp_allKeys[_begin_exp_allKeys.length - 1].name;  // just the last key pressed
        begin_exp.rt = _begin_exp_allKeys[_begin_exp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction__screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction__screenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instruction__screen'-------
    for (const thisComponent of Instruction__screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begin_exp.keys', begin_exp.keys);
    if (typeof begin_exp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('begin_exp.rt', begin_exp.rt);
        routineTimer.reset();
        }
    
    begin_exp.stop();
    // the Routine "Instruction__screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Baseline_trials;
var currentLoop;
function Baseline_trialsLoopBegin(Baseline_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Baseline_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'Baseline_trials'
    });
    psychoJS.experiment.addLoop(Baseline_trials); // add the loop to the experiment
    currentLoop = Baseline_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBaseline_trial of Baseline_trials) {
      const snapshot = Baseline_trials.getSnapshot();
      Baseline_trialsLoopScheduler.add(importConditions(snapshot));
      Baseline_trialsLoopScheduler.add(Baseline_codeRoutineBegin(snapshot));
      Baseline_trialsLoopScheduler.add(Baseline_codeRoutineEachFrame());
      Baseline_trialsLoopScheduler.add(Baseline_codeRoutineEnd());
      Baseline_trialsLoopScheduler.add(Baseline_StroopRoutineBegin(snapshot));
      Baseline_trialsLoopScheduler.add(Baseline_StroopRoutineEachFrame());
      Baseline_trialsLoopScheduler.add(Baseline_StroopRoutineEnd());
      Baseline_trialsLoopScheduler.add(endLoopIteration(Baseline_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function Baseline_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(Baseline_trials);

  return Scheduler.Event.NEXT;
}


var eo_trials;
function eo_trialsLoopBegin(eo_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    eo_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'eo_trials'
    });
    psychoJS.experiment.addLoop(eo_trials); // add the loop to the experiment
    currentLoop = eo_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisEo_trial of eo_trials) {
      const snapshot = eo_trials.getSnapshot();
      eo_trialsLoopScheduler.add(importConditions(snapshot));
      eo_trialsLoopScheduler.add(EO_CODERoutineBegin(snapshot));
      eo_trialsLoopScheduler.add(EO_CODERoutineEachFrame());
      eo_trialsLoopScheduler.add(EO_CODERoutineEnd());
      eo_trialsLoopScheduler.add(EO_ConditionRoutineBegin(snapshot));
      eo_trialsLoopScheduler.add(EO_ConditionRoutineEachFrame());
      eo_trialsLoopScheduler.add(EO_ConditionRoutineEnd());
      eo_trialsLoopScheduler.add(endLoopIteration(eo_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function eo_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(eo_trials);

  return Scheduler.Event.NEXT;
}


var fo_loop;
function fo_loopLoopBegin(fo_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    fo_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'fo_loop'
    });
    psychoJS.experiment.addLoop(fo_loop); // add the loop to the experiment
    currentLoop = fo_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFo_loop of fo_loop) {
      const snapshot = fo_loop.getSnapshot();
      fo_loopLoopScheduler.add(importConditions(snapshot));
      fo_loopLoopScheduler.add(FO_CODERoutineBegin(snapshot));
      fo_loopLoopScheduler.add(FO_CODERoutineEachFrame());
      fo_loopLoopScheduler.add(FO_CODERoutineEnd());
      fo_loopLoopScheduler.add(FO_ConditionRoutineBegin(snapshot));
      fo_loopLoopScheduler.add(FO_ConditionRoutineEachFrame());
      fo_loopLoopScheduler.add(FO_ConditionRoutineEnd());
      fo_loopLoopScheduler.add(endLoopIteration(fo_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function fo_loopLoopEnd() {
  psychoJS.experiment.removeLoop(fo_loop);

  return Scheduler.Event.NEXT;
}


var nf_trials;
function nf_trialsLoopBegin(nf_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nf_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 40, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nf_trials'
    });
    psychoJS.experiment.addLoop(nf_trials); // add the loop to the experiment
    currentLoop = nf_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNf_trial of nf_trials) {
      const snapshot = nf_trials.getSnapshot();
      nf_trialsLoopScheduler.add(importConditions(snapshot));
      nf_trialsLoopScheduler.add(NF_CODERoutineBegin(snapshot));
      nf_trialsLoopScheduler.add(NF_CODERoutineEachFrame());
      nf_trialsLoopScheduler.add(NF_CODERoutineEnd());
      nf_trialsLoopScheduler.add(NF_ConditionRoutineBegin(snapshot));
      nf_trialsLoopScheduler.add(NF_ConditionRoutineEachFrame());
      nf_trialsLoopScheduler.add(NF_ConditionRoutineEnd());
      nf_trialsLoopScheduler.add(endLoopIteration(nf_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function nf_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(nf_trials);

  return Scheduler.Event.NEXT;
}


var wordItem;
var wordColor;
var Baseline_codeComponents;
function Baseline_codeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Baseline_code'-------
    t = 0;
    Baseline_codeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    wordItem = all_word_lst[study_trial];
    wordColor = all_color_lst[study_trial];
    study_trial += 1;
    
    // keep track of which components have finished
    Baseline_codeComponents = [];
    
    for (const thisComponent of Baseline_codeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Baseline_codeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Baseline_code'-------
    // get current time
    t = Baseline_codeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Baseline_codeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Baseline_codeRoutineEnd() {
  return async function () {
    //------Ending Routine 'Baseline_code'-------
    for (const thisComponent of Baseline_codeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Baseline_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var Baseline_StroopComponents;
function Baseline_StroopRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Baseline_Stroop'-------
    t = 0;
    Baseline_StroopClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    baseline_stroop_word.setColor(new util.Color(WordColor));
    baseline_stroop_word.setText(WordItem);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    Baseline_StroopComponents = [];
    Baseline_StroopComponents.push(baseline_stroop_word);
    Baseline_StroopComponents.push(baseline_fixation);
    Baseline_StroopComponents.push(key_resp);
    
    for (const thisComponent of Baseline_StroopComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Baseline_StroopRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Baseline_Stroop'-------
    // get current time
    t = Baseline_StroopClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *baseline_stroop_word* updates
    if (t >= 1.5 && baseline_stroop_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      baseline_stroop_word.tStart = t;  // (not accounting for frame time here)
      baseline_stroop_word.frameNStart = frameN;  // exact frame index
      
      baseline_stroop_word.setAutoDraw(true);
    }

    frameRemains = 1.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (baseline_stroop_word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      baseline_stroop_word.setAutoDraw(false);
    }
    
    // *baseline_fixation* updates
    if (t >= 0.5 && baseline_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      baseline_fixation.tStart = t;  // (not accounting for frame time here)
      baseline_fixation.frameNStart = frameN;  // exact frame index
      
      baseline_fixation.setAutoDraw(true);
    }

    frameRemains = 0.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (baseline_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      baseline_fixation.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 1.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 1.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Baseline_StroopComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Baseline_StroopRoutineEnd() {
  return async function () {
    //------Ending Routine 'Baseline_Stroop'-------
    for (const thisComponent of Baseline_StroopComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var _proceed_to_conditions_allKeys;
var Begin_Video_obs_taskComponents;
function Begin_Video_obs_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Begin_Video_obs_task'-------
    t = 0;
    Begin_Video_obs_taskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    proceed_to_conditions.keys = undefined;
    proceed_to_conditions.rt = undefined;
    _proceed_to_conditions_allKeys = [];
    // keep track of which components have finished
    Begin_Video_obs_taskComponents = [];
    Begin_Video_obs_taskComponents.push(begin_video_obs);
    Begin_Video_obs_taskComponents.push(proceed_to_conditions);
    
    for (const thisComponent of Begin_Video_obs_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Begin_Video_obs_taskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Begin_Video_obs_task'-------
    // get current time
    t = Begin_Video_obs_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *begin_video_obs* updates
    if (t >= 0.5 && begin_video_obs.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_video_obs.tStart = t;  // (not accounting for frame time here)
      begin_video_obs.frameNStart = frameN;  // exact frame index
      
      begin_video_obs.setAutoDraw(true);
    }

    
    // *proceed_to_conditions* updates
    if (t >= 0.5 && proceed_to_conditions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceed_to_conditions.tStart = t;  // (not accounting for frame time here)
      proceed_to_conditions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { proceed_to_conditions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { proceed_to_conditions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { proceed_to_conditions.clearEvents(); });
    }

    if (proceed_to_conditions.status === PsychoJS.Status.STARTED) {
      let theseKeys = proceed_to_conditions.getKeys({keyList: ['right'], waitRelease: false});
      _proceed_to_conditions_allKeys = _proceed_to_conditions_allKeys.concat(theseKeys);
      if (_proceed_to_conditions_allKeys.length > 0) {
        proceed_to_conditions.keys = _proceed_to_conditions_allKeys[_proceed_to_conditions_allKeys.length - 1].name;  // just the last key pressed
        proceed_to_conditions.rt = _proceed_to_conditions_allKeys[_proceed_to_conditions_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Begin_Video_obs_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Begin_Video_obs_taskRoutineEnd() {
  return async function () {
    //------Ending Routine 'Begin_Video_obs_task'-------
    for (const thisComponent of Begin_Video_obs_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('proceed_to_conditions.keys', proceed_to_conditions.keys);
    if (typeof proceed_to_conditions.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('proceed_to_conditions.rt', proceed_to_conditions.rt);
        routineTimer.reset();
        }
    
    proceed_to_conditions.stop();
    // the Routine "Begin_Video_obs_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var eo_WordItem;
var eo_WordColor;
var eo_video;
var eo_WordType;
var eo_condition;
var EO_CODEComponents;
function EO_CODERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EO_CODE'-------
    t = 0;
    EO_CODEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    eo_WordItem = eo_word_lst[eo_trial];
    eo_WordColor = eo_color_lst[eo_trial];
    eo_video = videoA[eo_trial];
    eo_WordType = "undefined";
    if (_pj.in_es6(eo_WordItem, food)) {
        eo_WordType = "food";
    }
    if (_pj.in_es6(eo_WordItem, neutral)) {
        eo_WordType = "neutral";
    }
    eo_condition = "EO";
    psychoJS.experiment.addData("wordContent", eo_WordItem);
    psychoJS.experiment.addData("wordColor", eo_WordColor);
    psychoJS.experiment.addData("wordType", eo_WordType);
    psychoJS.experiment.addData("Condition", eo_condition);
    eo_trial += 1;
    
    // keep track of which components have finished
    EO_CODEComponents = [];
    
    for (const thisComponent of EO_CODEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EO_CODERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EO_CODE'-------
    // get current time
    t = EO_CODEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EO_CODEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EO_CODERoutineEnd() {
  return async function () {
    //------Ending Routine 'EO_CODE'-------
    for (const thisComponent of EO_CODEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "EO_CODE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var eo_videoClock;
var EO_ConditionComponents;
function EO_ConditionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EO_Condition'-------
    t = 0;
    EO_ConditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.500000);
    // update component parameters for each repeat
    eo_Stroop_word.setColor(new util.Color(eo_WordColor));
    eo_Stroop_word.setText(eo_WordItem);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    eo_videoClock = new util.Clock();
    eo_video = new visual.MovieStim({
      win: psychoJS.window,
      name: 'eo_video',
      units: undefined,
      movie: eo_video,
      pos: [0, 0],
      size: undefined,
      ori: 0.0,
      opacity: 1.0,
      loop: false,
      noAudio: true,
      });
    // keep track of which components have finished
    EO_ConditionComponents = [];
    EO_ConditionComponents.push(eo_Stroop_word);
    EO_ConditionComponents.push(eo_fixation_cross);
    EO_ConditionComponents.push(key_resp_2);
    EO_ConditionComponents.push(eo_video);
    
    for (const thisComponent of EO_ConditionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EO_ConditionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EO_Condition'-------
    // get current time
    t = EO_ConditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *eo_Stroop_word* updates
    if (t >= 4.5 && eo_Stroop_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eo_Stroop_word.tStart = t;  // (not accounting for frame time here)
      eo_Stroop_word.frameNStart = frameN;  // exact frame index
      
      eo_Stroop_word.setAutoDraw(true);
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (eo_Stroop_word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      eo_Stroop_word.setAutoDraw(false);
    }
    
    // *eo_fixation_cross* updates
    if (t >= 3.25 && eo_fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eo_fixation_cross.tStart = t;  // (not accounting for frame time here)
      eo_fixation_cross.frameNStart = frameN;  // exact frame index
      
      eo_fixation_cross.setAutoDraw(true);
    }

    frameRemains = 3.25 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (eo_fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      eo_fixation_cross.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (t >= 4.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *eo_video* updates
    if (t >= 0.5 && eo_video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      eo_video.tStart = t;  // (not accounting for frame time here)
      eo_video.frameNStart = frameN;  // exact frame index
      
      eo_video.setAutoDraw(true);
      eo_video.play();
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (eo_video.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      eo_video.setAutoDraw(false);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EO_ConditionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EO_ConditionRoutineEnd() {
  return async function () {
    //------Ending Routine 'EO_Condition'-------
    for (const thisComponent of EO_ConditionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    eo_video.stop();
    return Scheduler.Event.NEXT;
  };
}


var _end_break_allKeys;
var BreakComponents;
function BreakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Break'-------
    t = 0;
    BreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(600.500000);
    // update component parameters for each repeat
    end_break.keys = undefined;
    end_break.rt = undefined;
    _end_break_allKeys = [];
    // keep track of which components have finished
    BreakComponents = [];
    BreakComponents.push(Break_text);
    BreakComponents.push(end_break);
    
    for (const thisComponent of BreakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function BreakRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Break'-------
    // get current time
    t = BreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Break_text* updates
    if (t >= 0 && Break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Break_text.tStart = t;  // (not accounting for frame time here)
      Break_text.frameNStart = frameN;  // exact frame index
      
      Break_text.setAutoDraw(true);
    }

    frameRemains = 0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Break_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Break_text.setAutoDraw(false);
    }
    
    // *end_break* updates
    if (t >= 0.5 && end_break.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_break.tStart = t;  // (not accounting for frame time here)
      end_break.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_break.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_break.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_break.clearEvents(); });
    }

    frameRemains = 0.5 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_break.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_break.status = PsychoJS.Status.FINISHED;
  }

    if (end_break.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_break.getKeys({keyList: ['right'], waitRelease: false});
      _end_break_allKeys = _end_break_allKeys.concat(theseKeys);
      if (_end_break_allKeys.length > 0) {
        end_break.keys = _end_break_allKeys[_end_break_allKeys.length - 1].name;  // just the last key pressed
        end_break.rt = _end_break_allKeys[_end_break_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BreakComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BreakRoutineEnd() {
  return async function () {
    //------Ending Routine 'Break'-------
    for (const thisComponent of BreakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_break.keys', end_break.keys);
    if (typeof end_break.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_break.rt', end_break.rt);
        routineTimer.reset();
        }
    
    end_break.stop();
    return Scheduler.Event.NEXT;
  };
}


var _proceed_to_next_condition_allKeys;
var RemainderComponents;
function RemainderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Remainder'-------
    t = 0;
    RemainderClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    proceed_to_next_condition.keys = undefined;
    proceed_to_next_condition.rt = undefined;
    _proceed_to_next_condition_allKeys = [];
    // keep track of which components have finished
    RemainderComponents = [];
    RemainderComponents.push(stroop_remainder);
    RemainderComponents.push(proceed_to_next_condition);
    
    for (const thisComponent of RemainderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RemainderRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Remainder'-------
    // get current time
    t = RemainderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stroop_remainder* updates
    if (t >= 0.0 && stroop_remainder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stroop_remainder.tStart = t;  // (not accounting for frame time here)
      stroop_remainder.frameNStart = frameN;  // exact frame index
      
      stroop_remainder.setAutoDraw(true);
    }

    
    // *proceed_to_next_condition* updates
    if (t >= 0.5 && proceed_to_next_condition.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceed_to_next_condition.tStart = t;  // (not accounting for frame time here)
      proceed_to_next_condition.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { proceed_to_next_condition.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { proceed_to_next_condition.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { proceed_to_next_condition.clearEvents(); });
    }

    if (proceed_to_next_condition.status === PsychoJS.Status.STARTED) {
      let theseKeys = proceed_to_next_condition.getKeys({keyList: ['right'], waitRelease: false});
      _proceed_to_next_condition_allKeys = _proceed_to_next_condition_allKeys.concat(theseKeys);
      if (_proceed_to_next_condition_allKeys.length > 0) {
        proceed_to_next_condition.keys = _proceed_to_next_condition_allKeys[_proceed_to_next_condition_allKeys.length - 1].name;  // just the last key pressed
        proceed_to_next_condition.rt = _proceed_to_next_condition_allKeys[_proceed_to_next_condition_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RemainderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RemainderRoutineEnd() {
  return async function () {
    //------Ending Routine 'Remainder'-------
    for (const thisComponent of RemainderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('proceed_to_next_condition.keys', proceed_to_next_condition.keys);
    if (typeof proceed_to_next_condition.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('proceed_to_next_condition.rt', proceed_to_next_condition.rt);
        routineTimer.reset();
        }
    
    proceed_to_next_condition.stop();
    // the Routine "Remainder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fo_WordItem;
var fo_WordColor;
var fo_video;
var fo_WordType;
var fo_condition;
var FO_CODEComponents;
function FO_CODERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FO_CODE'-------
    t = 0;
    FO_CODEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    fo_WordItem = fo_word_lst[fo_trial];
    fo_WordColor = fo_color_lst[fo_trial];
    fo_video = videoB[fo_trial];
    fo_WordType = "undefined";
    if (_pj.in_es6(fo_WordItem, food)) {
        fo_WordType = "food";
    }
    if (_pj.in_es6(fo_WordItem, neutral)) {
        fo_WordType = "neutral";
    }
    fo_condition = "FO";
    psychoJS.experiment.addData("wordContent", fo_WordItem);
    psychoJS.experiment.addData("wordColor", fo_WordColor);
    psychoJS.experiment.addData("wordType", fo_WordType);
    psychoJS.experiment.addData("Condition", fo_condition);
    fo_trial += 1;
    
    // keep track of which components have finished
    FO_CODEComponents = [];
    
    for (const thisComponent of FO_CODEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FO_CODERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FO_CODE'-------
    // get current time
    t = FO_CODEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FO_CODEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FO_CODERoutineEnd() {
  return async function () {
    //------Ending Routine 'FO_CODE'-------
    for (const thisComponent of FO_CODEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "FO_CODE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fo_videoClock;
var _key_resp_3_allKeys;
var FO_ConditionComponents;
function FO_ConditionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FO_Condition'-------
    t = 0;
    FO_ConditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.500000);
    // update component parameters for each repeat
    fo_videoClock = new util.Clock();
    fo_video = new visual.MovieStim({
      win: psychoJS.window,
      name: 'fo_video',
      units: undefined,
      movie: fo_video,
      pos: [0, 0],
      size: undefined,
      ori: 0.0,
      opacity: undefined,
      loop: false,
      noAudio: false,
      });
    fo_word.setColor(new util.Color(fo_WordColor));
    fo_word.setText(fo_WordItem);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    FO_ConditionComponents = [];
    FO_ConditionComponents.push(fo_video);
    FO_ConditionComponents.push(fo_fixation_cross);
    FO_ConditionComponents.push(fo_word);
    FO_ConditionComponents.push(key_resp_3);
    
    for (const thisComponent of FO_ConditionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FO_ConditionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FO_Condition'-------
    // get current time
    t = FO_ConditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fo_video* updates
    if (t >= 0.5 && fo_video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fo_video.tStart = t;  // (not accounting for frame time here)
      fo_video.frameNStart = frameN;  // exact frame index
      
      fo_video.setAutoDraw(true);
      fo_video.play();
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fo_video.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fo_video.setAutoDraw(false);
    }

    
    // *fo_fixation_cross* updates
    if (t >= 3.25 && fo_fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fo_fixation_cross.tStart = t;  // (not accounting for frame time here)
      fo_fixation_cross.frameNStart = frameN;  // exact frame index
      
      fo_fixation_cross.setAutoDraw(true);
    }

    frameRemains = 3.25 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fo_fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fo_fixation_cross.setAutoDraw(false);
    }
    
    // *fo_word* updates
    if (t >= 4.5 && fo_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fo_word.tStart = t;  // (not accounting for frame time here)
      fo_word.frameNStart = frameN;  // exact frame index
      
      fo_word.setAutoDraw(true);
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fo_word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fo_word.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 4.5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FO_ConditionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FO_ConditionRoutineEnd() {
  return async function () {
    //------Ending Routine 'FO_Condition'-------
    for (const thisComponent of FO_ConditionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    fo_video.stop();
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var nf_WordItem;
var nf_WordColor;
var nf_video;
var nf_WordType;
var nf_condition;
var NF_CODEComponents;
function NF_CODERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'NF_CODE'-------
    t = 0;
    NF_CODEClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    nf_WordItem = nf_word_lst[nf_trial];
    nf_WordColor = nf_color_lst[nf_trial];
    nf_video = videoC[nf_trial];
    nf_WordType = "undefined";
    if (_pj.in_es6(nf_WordItem, food)) {
        nf_WordType = "food";
    }
    if (_pj.in_es6(nf_WordItem, neutral)) {
        nf_WordType = "neutral";
    }
    nf_condition = "NF";
    psychoJS.experiment.addData("wordContent", nf_WordItem);
    psychoJS.experiment.addData("wordColor", nf_WordColor);
    psychoJS.experiment.addData("wordType", nf_WordType);
    psychoJS.experiment.addData("Condition", nf_condition);
    nf_trial += 1;
    
    // keep track of which components have finished
    NF_CODEComponents = [];
    
    for (const thisComponent of NF_CODEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NF_CODERoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'NF_CODE'-------
    // get current time
    t = NF_CODEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NF_CODEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NF_CODERoutineEnd() {
  return async function () {
    //------Ending Routine 'NF_CODE'-------
    for (const thisComponent of NF_CODEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "NF_CODE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var nf_videoClock;
var _key_resp_4_allKeys;
var NF_ConditionComponents;
function NF_ConditionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'NF_Condition'-------
    t = 0;
    NF_ConditionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.500000);
    // update component parameters for each repeat
    nf_videoClock = new util.Clock();
    nf_video = new visual.MovieStim({
      win: psychoJS.window,
      name: 'nf_video',
      units: undefined,
      movie: nf_video,
      pos: [0, 0],
      size: undefined,
      ori: 0.0,
      opacity: undefined,
      loop: false,
      noAudio: false,
      });
    nf_word.setColor(new util.Color(nf_WordColor));
    nf_word.setText(nf_WordItem);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    NF_ConditionComponents = [];
    NF_ConditionComponents.push(nf_video);
    NF_ConditionComponents.push(nf_fixation_cross);
    NF_ConditionComponents.push(nf_word);
    NF_ConditionComponents.push(key_resp_4);
    
    for (const thisComponent of NF_ConditionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function NF_ConditionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'NF_Condition'-------
    // get current time
    t = NF_ConditionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *nf_video* updates
    if (t >= 0.5 && nf_video.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nf_video.tStart = t;  // (not accounting for frame time here)
      nf_video.frameNStart = frameN;  // exact frame index
      
      nf_video.setAutoDraw(true);
      nf_video.play();
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (nf_video.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nf_video.setAutoDraw(false);
    }

    
    // *nf_fixation_cross* updates
    if (t >= 3.25 && nf_fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nf_fixation_cross.tStart = t;  // (not accounting for frame time here)
      nf_fixation_cross.frameNStart = frameN;  // exact frame index
      
      nf_fixation_cross.setAutoDraw(true);
    }

    frameRemains = 3.25 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (nf_fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nf_fixation_cross.setAutoDraw(false);
    }
    
    // *nf_word* updates
    if (t >= 4.5 && nf_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nf_word.tStart = t;  // (not accounting for frame time here)
      nf_word.frameNStart = frameN;  // exact frame index
      
      nf_word.setAutoDraw(true);
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (nf_word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      nf_word.setAutoDraw(false);
    }
    
    // *key_resp_4* updates
    if (t >= 4.5 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    frameRemains = 4.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of NF_ConditionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function NF_ConditionRoutineEnd() {
  return async function () {
    //------Ending Routine 'NF_Condition'-------
    for (const thisComponent of NF_ConditionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    nf_video.stop();
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    return Scheduler.Event.NEXT;
  };
}


var _end_key_allKeys;
var Thank_youComponents;
function Thank_youRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Thank_you'-------
    t = 0;
    Thank_youClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_key.keys = undefined;
    end_key.rt = undefined;
    _end_key_allKeys = [];
    // keep track of which components have finished
    Thank_youComponents = [];
    Thank_youComponents.push(text);
    Thank_youComponents.push(end_key);
    
    for (const thisComponent of Thank_youComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Thank_youRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Thank_you'-------
    // get current time
    t = Thank_youClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *end_key* updates
    if (t >= 0.5 && end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_key.tStart = t;  // (not accounting for frame time here)
      end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_key.clearEvents(); });
    }

    if (end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_key.getKeys({keyList: ['space'], waitRelease: false});
      _end_key_allKeys = _end_key_allKeys.concat(theseKeys);
      if (_end_key_allKeys.length > 0) {
        end_key.keys = _end_key_allKeys[_end_key_allKeys.length - 1].name;  // just the last key pressed
        end_key.rt = _end_key_allKeys[_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Thank_youComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Thank_youRoutineEnd() {
  return async function () {
    //------Ending Routine 'Thank_you'-------
    for (const thisComponent of Thank_youComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_key.keys', end_key.keys);
    if (typeof end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_key.rt', end_key.rt);
        routineTimer.reset();
        }
    
    end_key.stop();
    // the Routine "Thank_you" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
