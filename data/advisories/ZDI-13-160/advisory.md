# ZDI-13-160: Oracle Java Sequencer Security Manager Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-160
- **ZDI-CAN:** ZDI-CAN-1795
- **Date:** 2013-06-27
- **CVE:** CVE-2013-2448
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the javax.sound.midi.Sequence class. The issue lies in the ability to create an event listener that is run in a privileged context. An attacker can leverage this to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
