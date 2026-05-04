# ZDI-17-828: Trend Micro OfficeScan tmwfp Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-828
- **ZDI-CAN:** ZDI-CAN-5068
- **Date:** 2017-09-27
- **CVE:** CVE-2017-14088
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** zer0b4by
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-828/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Trend Micro OfficeScan. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x220008 within tmwfp.sys. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to escalate privileges to resources normally reserved for the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1118372

## Disclosure Timeline

- 2017-09-05 - Vulnerability reported to vendor
- 2017-09-27 - Coordinated public release of advisory
