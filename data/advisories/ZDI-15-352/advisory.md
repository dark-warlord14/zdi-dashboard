# ZDI-15-352: Oracle Endeca Information Discovery Integrator ETL Server RenameFile Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-352
- **ZDI-CAN:** ZDI-CAN-2775
- **Date:** 2015-07-20
- **CVE:** CVE-2015-2606
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Endeca Tools and Frameworks
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-352/
## Vulnerability Details

This vulnerability allows remote attackers the ability to execute arbitrary code on vulnerable instances of Oracle Endeca Information Discovery. Authentication is required to exploit this vulnerability but an authentication bypass is known. The specific flaw exists in the handling of the RenameFile endpoint. The issue lies in the failure to properly sanitize the path of files. A remote attacker can exploit this vulnerability to read server configuration files. This exfiltrated information can then be used to access the system with the privileges of the clover server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujul2015-2367936.html

## Disclosure Timeline

- 2015-02-25 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
