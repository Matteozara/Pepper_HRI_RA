<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Pepper_dialog" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="freeSpaces" src="freeSpaces/freeSpaces.dlg" />
    </Dialogs>
    <Resources>
        <File name="surprise3" src="behavior_1/surprise3.ogg" />
        <File name="forward_4m" src="forward_4m.pmt" />
        <File name="forward_10" src="forward_10.pmt" />
        <File name="forward_5" src="forward_5.pmt" />
        <File name="forward_2" src="forward_2.pmt" />
        <File name="ExampleDialotg2" src="ExampleDialotg2" />
        <File name="forward_15" src="forward_15.pmt" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="freeSpaces_enu" src="freeSpaces/freeSpaces_enu.top" topicName="freeSpaces" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
