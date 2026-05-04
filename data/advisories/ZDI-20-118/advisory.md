# ZDI-20-118: Cisco Data Center Network Manager getDeployContent Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-118
- **ZDI-CAN:** ZDI-CAN-9469
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15980
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-118/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of requests to the rest/auto-config/fabrics/abc/deployments/files endpoint. When parsing the full URL, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker could leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-path-trav

## Disclosure Timeline

- 2019-10-22 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
