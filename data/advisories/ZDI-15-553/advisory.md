# ZDI-15-553: IBM System Networking Switch Center FileReader.jsp Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-553
- **ZDI-CAN:** ZDI-CAN-3012
- **Date:** 2015-11-10
- **CVE:** CVE-2015-7817
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** System Networking Switch Center
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-553/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on vulnerable installations of IBM System Networking Switch Center. Authentication is not required to exploit this vulnerability. The specific flaws exist within the IBM SNSC Web Service, which listens by default on ports 40080 (HTTP) or 40443 (HTTPS) for requests to the administration panel. The first is a race condition, which allows the for the temporary use of a fixed privileged account which is forbidden from interactive login, and the second is a directory traversal vulnerability in FileReader.jsp. By combining these two vulnerabilities, an attacker can read arbitrary text files on the system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://support.lenovo.com/us/en/product_security/len_2015_074

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
