# ZDI-24-1741: WSO2 API Manager SynapseArtifactUploaderAdmin Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1741
- **ZDI-CAN:** ZDI-CAN-26065
- **Date:** 2024-12-30
- **CVE:** CVE-2024-7074
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WSO2
- **Affected Products:** API Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1741/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WSO2 API Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the SynapseArtifactUploaderAdmin endpoint, which listens on TCP port 9443 by default. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

WSO2 has issued an update to correct this vulnerability. More details can be found at: https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2024/WSO2-2024-3566/

## Disclosure Timeline

- 2024-12-19 - Vulnerability reported to vendor
- 2024-12-30 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
