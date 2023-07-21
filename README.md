# Port-Test-Programm - Eine ausführliche Beschreibung

## Einführung
Das Port-Test-Programm ist ein Python-Skript, das es dem Benutzer ermöglicht, die Erreichbarkeit eines bestimmten Netzwerkports auf einer angegebenen IP-Adresse zu überprüfen. Das Skript verwendet die Socket-Bibliothek, um eine Verbindung zum angegebenen Host und Port herzustellen und festzustellen, ob die Verbindung erfolgreich hergestellt werden konnte.

## Funktionsweise
Das Skript beginnt mit der Definition einer ASCII Art, die dem Benutzer eine Willkommensnachricht mit dem Namen des Skripts vermittelt. Die ASCII Art ist ein stilisiertes Logo, das den Namen "Port-Test-Programm" darstellt.

Der Benutzer wird dann aufgefordert, die IP-Adresse und den Port einzugeben, den er überprüfen möchte. Dazu verwendet das Skript die `input()`-Funktion, um die Benutzereingaben abzurufen.

Anschließend wird eine `is_port_open(ip, port)` Funktion definiert, die versucht, eine Verbindung zum angegebenen Host und Port herzustellen. Die Funktion verwendet die `socket`-Bibliothek und den `socket.AF_INET` Adressfamilientyp und den `socket.SOCK_STREAM` Sockettyp, um eine TCP-Verbindung herzustellen. Mit `socket.settimeout(1)` wird eine Zeitüberschreitung von 1 Sekunde festgelegt, um lange Wartezeiten zu verhindern. Die Funktion gibt `True` zurück, wenn die Verbindung erfolgreich hergestellt wurde (der Port ist geöffnet) und `False`, wenn die Verbindung fehlgeschlagen ist (der Port ist geschlossen).

Im Hauptteil des Skripts wird die `main()`-Funktion definiert, die die Benutzereingaben abruft und den Port-Test durchführt. Die ASCII Art wird ausgegeben, um den Benutzer zu begrüßen.

Anschließend wird eine Endlosschleife verwendet, die den Port kontinuierlich in regelmäßigen Abständen überprüft. Nach jeder Überprüfung wird der Benutzer aufgefordert, "q" zu drücken, um den Test zu beenden, oder Enter, um den Test fortzusetzen. Der Test läuft solange, bis der Benutzer "q" eingibt.

Das Skript ermöglicht es dem Benutzer, die Erreichbarkeit eines Netzwerkports auf einer angegebenen IP-Adresse kontinuierlich zu überwachen und zu testen.
