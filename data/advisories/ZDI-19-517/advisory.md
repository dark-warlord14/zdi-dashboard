# ZDI-19-517: Fuji Electric Alpha7 PC Loader A7P File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-517
- **ZDI-CAN:** ZDI-CAN-8030
- **Date:** 2019-05-29
- **CVE:** CVE-2019-10975
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha7
- **Credit:** kimiya of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-517/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Fuji Electric Alpha7. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of A7P files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the Administrator.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-136-02

## Disclosure Timeline

- 2019-03-15 - Vulnerability reported to vendor
- 2019-05-29 - Coordinated public release of advisory
