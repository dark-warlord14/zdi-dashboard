# ZDI-18-1273: Oracle Outside In vsxl5 GelFrame Record Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1273
- **ZDI-CAN:** ZDI-CAN-7075
- **Date:** 2018-10-17
- **CVE:** CVE-2018-3147
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Outside In
- **Credit:** Kamlapati Choubey of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1273/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Oracle Outside In. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within vsxl5.dll. When parsing the GelFrame record, the process does not properly validate user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose sensitive information in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html

## Disclosure Timeline

- 2018-08-10 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
