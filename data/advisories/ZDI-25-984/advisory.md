# ZDI-25-984: Alibaba Cloud Workspace Client Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-984
- **ZDI-CAN:** ZDI-CAN-26635
- **Date:** 2025-10-30
- **CVE:** N/A
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alibaba
- **Affected Products:** Cloud Workspace Client
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-984/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Alibaba Cloud Workspace Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Fixed in Wuying Client v7.10. https://www.aliyun.com/product/wuying/download

## Disclosure Timeline

- 2025-03-13 - Vulnerability reported to vendor
- 2025-10-30 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated
