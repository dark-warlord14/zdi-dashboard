# ZDI-20-014: Cisco Data Center Network Manager ReportWS deleteReportTemplate Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-014
- **ZDI-CAN:** ZDI-CAN-9130
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15981
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-014/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SOAP deleteReportTemplate endpoint of the ReportWSService/ReportWS path in the service. When parsing the reportTemplateName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM and to create a denial-of-service condition.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-path-trav

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
