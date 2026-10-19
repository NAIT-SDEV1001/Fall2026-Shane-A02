def display_game_settings(**settings):
    print("Game settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
    print(f"Setting count: {len(settings)}")

display_game_settings(difficulty="easy", sound=True, lives=3)