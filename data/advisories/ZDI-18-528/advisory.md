# ZDI-18-528: Micro Focus Client for Open Enterprise Server Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-528
- **ZDI-CAN:** ZDI-CAN-5479
- **Date:** 2018-05-22
- **CVE:** CVE-2018-7687
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Micro Focus
- **Affected Products:** Client for Open Enterprise Server
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-528/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Micro Focus Client for Open Enterprise Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x143CFB. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7022983

## Disclosure Timeline

- 2017-12-21 - Vulnerability reported to vendor
- 2018-05-22 - Coordinated public release of advisory
- 2018-05-22 - Advisory Updated
