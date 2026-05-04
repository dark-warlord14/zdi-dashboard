# ZDI-18-410: Trend Micro Maximum Security tmusa Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-410
- **ZDI-CAN:** ZDI-CAN-5500
- **Date:** 2018-05-04
- **CVE:** CVE-2018-6236
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-410/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x222813 by the tmusa driver. The code is subject to a time-of-check/time-of-use race condition when processing data from the user. An attacker can leverage this vulnerability to escalate privileges to kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1119591.aspx

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
