# ZDI-17-1017: Huawei Mate 9 Pro Mali Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-1017
- **ZDI-CAN:** ZDI-CAN-5337
- **Date:** 2018-06-08
- **CVE:** CVE-2017-15316
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Huawei
- **Affected Products:** Mate 9 Pro
- **Credit:** Tencent Keen Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-1017/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Huawei Mate 9 Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Mali GPU driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the kernel.

## Additional Details

Huawei has issued an update to correct this vulnerability. More details can be found at: http://www.huawei.com/en/psirt/security-advisories/huawei-sa-20171201-01-smartphone-en

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-08 - Coordinated public release of advisory
- 2018-06-08 - Advisory Updated
