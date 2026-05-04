# ZDI-15-356: Oracle Endeca Information Discovery Integrator ETL Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-356
- **ZDI-CAN:** ZDI-CAN-2771
- **Date:** 2015-07-20
- **CVE:** CVE-2015-2603
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Endeca Tools and Frameworks
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-356/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Oracle Endeca Information Discovery. Authentication is not required to exploit this vulnerability. The specific flaw exists within the generation and use of session hashes. The issue lies in the use of the fixed data when authenticating. An attacker can leverage this vulnerability to bypass authentication checks which can then be chained to execute code within the context of the clover service.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujul2015-2367936.html

## Disclosure Timeline

- 2015-02-25 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
