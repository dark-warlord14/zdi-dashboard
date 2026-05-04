# ZDI-23-589: Trend Micro Mobile Security for Enterprises widget set_certificates_config Unrestricted File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-589
- **ZDI-CAN:** ZDI-CAN-20179
- **Date:** 2023-05-12
- **CVE:** CVE-2023-32525
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprises
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-589/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Trend Micro Mobile Security for Enterprises. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the set_certificates_config action defined within the web/widget path. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293106

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-05-12 - Coordinated public release of advisory
