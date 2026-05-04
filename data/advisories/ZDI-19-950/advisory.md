# ZDI-19-950: Advantech WISE-PaaS/RMM UpgradeMgmt upload_ota Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-950
- **ZDI-CAN:** ZDI-CAN-9173
- **Date:** 2019-11-01
- **CVE:** CVE-2019-13551
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WISE-PaaS/RMM
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-950/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WISE-PasS/RMM. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the UpgradeMgmt class. When parsing the frmUpdateSetting_UploadFileFullName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-304-01

## Disclosure Timeline

- 2019-08-20 - Vulnerability reported to vendor
- 2019-11-01 - Coordinated public release of advisory
