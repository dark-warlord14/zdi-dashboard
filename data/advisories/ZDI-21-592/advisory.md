# ZDI-21-592: QNAP NAS Malware Remover Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-592
- **ZDI-CAN:** ZDI-CAN-12891
- **Date:** 2021-05-14
- **CVE:** CVE-2020-36198
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** NAS
- **Credit:** polict of Shielder
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-592/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of QNAP NAS. Authentication is required to exploit this vulnerability. The specific flaw exists within the Malware Remover application. A crafted TAR file in the file system can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the admin user.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/zh-tw/security-advisory/qsa-21-16

## Disclosure Timeline

- 2021-01-22 - Vulnerability reported to vendor
- 2021-05-14 - Coordinated public release of advisory
