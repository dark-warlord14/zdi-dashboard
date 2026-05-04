# ZDI-14-267: Shunra Network Virtualization for Hewlett-Packard storedNtxFile() Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-267
- **ZDI-CAN:** ZDI-CAN-2023
- **Date:** 2014-07-24
- **CVE:** CVE-2014-2625
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Network Virtualization
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-267/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Network Visualization. Authentication is not required to exploit this vulnerability. The specific flaw exists within the storedNtxFile function. The method does not properly sanitize the input to this function allowing for directory traversal. An attacker can leverage this vulnerability to read files from the remote system.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04374202

## Disclosure Timeline

- 2014-04-08 - Vulnerability reported to vendor
- 2014-07-24 - Coordinated public release of advisory
