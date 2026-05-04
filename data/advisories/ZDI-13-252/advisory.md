# ZDI-13-252: Cogent DataHub Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-252
- **ZDI-CAN:** ZDI-CAN-1981
- **Date:** 2013-11-24
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cogent Real-Time Systems
- **Affected Products:** Cogent Datahub
- **Credit:** Pawel Wylecial
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-252/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cogent DataHub. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of POST requests. By sending a malformed POST, an attacker is able to overflow a heap buffer. An attacker could exploit this vulnerability to execute arbitrary code in the context of the DataHub process.

## Additional Details

Cogent Real-Time Systems has issued an update to correct this vulnerability. More details can be found at: http://www.cogentdatahub.com/Download_Software.html

## Disclosure Timeline

- 2013-09-06 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
