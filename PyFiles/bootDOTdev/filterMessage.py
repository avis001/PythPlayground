def filter_messages(messages):
    cMessages = []
    slurredCount = []

    for eachMessage in messages:
        words = eachMessage.split()
        slurred = 0

        for index, eachWord in enumerate(words):
            if eachWord == "dang":
                del words[index]
                slurred += 1

        cMessages.append(" ".join(words))
        slurredCount.append(slurred)

    return cMessages, slurredCount


def main():
    cMessages, slurredCount = filter_messages(
        [
            "That's the bloody dang Reaper of Mars...",
            "Pax au Telemanus!",
            "I was never taught how to use a dang razor!",
        ]
    )
    print(f"Messages: {cMessages} \n")
    print(f"Cuont: {slurredCount} \n")


main()
