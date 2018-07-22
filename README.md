# hipchat2zulip, a hipchat to zulip bridge

This is a simple hipchat bot (strictly, a plugin) powered by [errbot](http://errbot.io) that simply forward any message
sent to the channel it's suscribed to a Zulip stream.

## How to setup and run

- Clone the repo or download the zip and uncompress it.
- Install the requirements `pip install -r requirements.txt`
- Then, configure errbot with hipchat backend, following the [errbot's doc](http://errbot.io/en/latest/user_guide/configuration/hipchat.html).
  To do this, create a module named `local_settings.py` with your custom settings.

  Mandatory settings are the following:

    - `BOT_IDENTITY`: jabber credentials + full permission token)
    - `CHATROOM_FN`: bot name, as defined in its profile. I named it *Zulip*
    - `CHATROOM_PRESENCE`: Channels to join (i.e. channels to forward

- In Zulip, [create a generic bot](https://zulipchat.com/help/add-a-bot-or-integration). With its data (email, token) define a `plugins/zuliprc`
file. You can rename `zuliprc.template` as example, or directly download the bot's API configuration file and rename it.

- Also, you need to create a new stream named `Hipchat`, and subscribe your bot to it.

- You are done. Run the bot:

    ```
    $ errbot --config config.py
    ```

After join each channel, every message received by the bot should be streamed to zulip's *Hipchat* stream, using the hipchat channel's name as zulip's topic, with the form `<Hipchat nick>: <message>`.


## Why?

This is a proof of concept that was done as a little effort to break the inertia and ease the move of [Onapsis](http://onapsis.com)'s Engineering from Hipchat 💩 to Zulip 😎.





