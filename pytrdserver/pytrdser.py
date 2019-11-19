from flask import Flask, render_template
from dcs_finite_state_machine import dcs

app = Flask(__name__)

fsms = [dcs]

fsms = {fsm.name: fsm for fsm in fsms}

@app.route('/<fsm_name>/status')
def get_fsm_status(fsm_name):
    fsm = fsms[fsm_name]
    return str(fsm.state)

@app.route('/<fsm_name>/run_cmd/<cmd_i>')
def run_fsm_cmd(fsm_name, cmd_i):
    fsm = fsms[fsm_name]
    cmd = fsm.state.cmds[int(cmd_i)]
    ncmds = fsm.run_cmd(cmd)

    return render_template('run_cmds.html', fsm=fsm, cmds=[(i, ncmds[i]) for i in range(len(ncmds))])

@app.route('/<fsm_name>/get_commands')
def get_fsm_commands(fsm_name):
    fsm = fsms[fsm_name]
    return str([(i, str(fsm.state.cmds[i])) for i in range(len(fsm.state.cmds))])

@app.route('/<fsm_name>')
def fsm_home(fsm_name):
    fsm = fsms[fsm_name]
    cmds = fsm.state.cmds
    return render_template('run_cmds.html', fsm=fsm, cmds=[(i, cmds[i]) for i in range(len(cmds))])

if __name__=='__main__':
    app.run(host='0.0.0.0')
