# ZDI-17-396: Trend Micro Maximum Security tmusa Time-Of-Check/Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-396
- **ZDI-CAN:** ZDI-CAN-4065
- **Date:** 2017-06-13
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-396/
## Vulnerability Details

This vulnerability allows local attackers to escalate privilege on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x222813. The issue results from a time-of-check/time-of-use vulnerability, which allows an attacker to change a field that is being used by the kernel. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117509

## Disclosure Timeline

- 2017-03-28 - Vulnerability reported to vendor
- 2017-06-13 - Coordinated public release of advisory
