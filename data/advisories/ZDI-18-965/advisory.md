# ZDI-18-965: Linux Kernel MIDI Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-965
- **ZDI-CAN:** ZDI-CAN-6201
- **Date:** 2018-08-30
- **CVE:** CVE-2018-10902
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Linux
- **Affected Products:** Linux Kernel
- **Credit:** 9462acee94608ea1643688d026aa95dd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-965/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of MIDI devices. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges to the level of kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=1590720

## Disclosure Timeline

- 2018-06-13 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
