# ZDI-17-490: Apple iTunes iPodService Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-490
- **ZDI-CAN:** ZDI-CAN-4798
- **Date:** 2017-07-19
- **CVE:** CVE-2017-7053
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** iTunes
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-490/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple iTunes. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the iPodManager COM control. The issue results from the lack of proper restriction of access to the control. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of SYSTEM.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-05-06 - Vulnerability reported to vendor
- 2017-07-19 - Coordinated public release of advisory
