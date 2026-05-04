# ZDI-14-118: InduSoft Web Studio Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-118
- **ZDI-CAN:** ZDI-CAN-2108
- **Date:** 2014-05-02
- **CVE:** CVE-2014-0780
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-118/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Indusoft Web Studio. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ability to browse outside of the web root via directory traversal. A remote attacker can abuse this to download sensitive files and execute remote code under the context of the user.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-107-02

## Disclosure Timeline

- 2014-01-30 - Vulnerability reported to vendor
- 2014-05-02 - Coordinated public release of advisory
