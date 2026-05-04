# ZDI-23-1064: (0Day) Softing Secure Integration Server Hardcoded Cryptographic Key Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1064
- **ZDI-CAN:** ZDI-CAN-20610
- **Date:** 2023-08-09
- **CVE:** CVE-2023-39482
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Uri Katz of Claroty Research Team82
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1064/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Softing Secure Integration Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within libopcuaclient.so. The issue results from hardcoding crytographic keys within the product. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

03/15/23 – The ZDI reported the vulnerability to the vendor. 07/31/23 – ZDI asked for an update. 08/03/23 – ZDI asked for an update. 08/07/23 – The ZDI asked for an update and informed the vendor that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-03-15 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
