# ZDI-18-564: Trend Micro OfficeScan TMWFP driver Pool Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-564
- **ZDI-CAN:** ZDI-CAN-5638
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10359
- **CVSS:** 5.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:N/I:P/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-564/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro OfficeScan. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x220078 in the TMWFP driver. The issue results from the lack of proper validation of the length of user-supplied data prior to using that length to initialize a pool-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119961

## Disclosure Timeline

- 2018-02-02 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
