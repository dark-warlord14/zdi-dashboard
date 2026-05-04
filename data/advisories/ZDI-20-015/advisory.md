# ZDI-20-015: Cisco Data Center Network Manager readConfigFileFromDB Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-015
- **ZDI-CAN:** ZDI-CAN-9139
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15981
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-015/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the readConfigFileFromDB SOAP endpoint called by accessing the WebAnalysisWSService/WebAnalysis path in the service. When parsing the configFileName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this to disclose files in the context of SYSTEM.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-path-trav

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
