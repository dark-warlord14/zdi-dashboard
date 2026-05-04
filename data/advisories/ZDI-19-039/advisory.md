# ZDI-19-039: Oracle Outside In vsxl5 GelFrame Record Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-039
- **ZDI-CAN:** ZDI-CAN-7592
- **Date:** 2019-01-17
- **CVE:** CVE-2018-3147
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** Kamlapati Choubey of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-039/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Oracle Outside In. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within vsxl5.dll. When parsing the GelFrame record, the process does not properly validate user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujan2019-5072801.html

## Disclosure Timeline

- 2018-11-22 - Vulnerability reported to vendor
- 2019-01-17 - Coordinated public release of advisory
