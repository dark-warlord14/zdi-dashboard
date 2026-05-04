# ZDI-20-1285: Trend Micro Antivirus for Mac Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1285
- **ZDI-CAN:** ZDI-CAN-11045
- **Date:** 2020-10-26
- **CVE:** CVE-2020-27014
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Cees Elzinga from Danish Cyber Defence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1285/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Antivirus for Mac. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the KERedirect kext. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-09974

## Disclosure Timeline

- 2020-06-24 - Vulnerability reported to vendor
- 2020-10-26 - Coordinated public release of advisory
