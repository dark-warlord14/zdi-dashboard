# ZDI-23-501: (Pwn2Own) NETGEAR RAX30 Device Configuration Cleartext Storage Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-501
- **ZDI-CAN:** ZDI-CAN-19841
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27370
- **CVSS:** 5.7
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-501/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of NETGEAR RAX30 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of device configuration. The issue results from the storage of configuration secrets in plaintext. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065619/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0348

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
