# ZDI-17-918: Cisco Prime Network Analysis Module graph sfile Parameter Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-918
- **ZDI-CAN:** ZDI-CAN-4918
- **Date:** 2017-11-20
- **CVE:** CVE-2017-12285
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** Prime Network Analysis Module
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-918/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Cisco Prime Network Analysis Module. Authentication is not required to exploit this vulnerability. The specific flaw exists within graph.php. When parsing the sfile parameter, the script does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any files accessible to the web service.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171018-nam

## Disclosure Timeline

- 2017-07-06 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
