# ZDI-11-024: Hewlett-Packard Data Protector Cell Manager Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-11-024
- **ZDI-CAN:** ZDI-CAN-722
- **Date:** 2011-01-20
- **CVE:** CVE-2011-0273
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Anonymous AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Data Protector Cell Manager. Authentication is not required to exploit these vulnerabilities. The specific flaws exist within the crs.exe process which listens on a random TCP port. The process fails to properly handle multiple message types and copies user-supplied data into fixed-length buffers. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02688353

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2011-01-20 - Coordinated public release of advisory
