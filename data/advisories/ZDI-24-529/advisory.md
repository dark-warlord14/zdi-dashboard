# ZDI-24-529: (Pwn2Own) VMware Workstation UrbBuf_getDataBuf Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-529
- **ZDI-CAN:** ZDI-CAN-23782
- **Date:** 2024-05-31
- **CVE:** CVE-2024-22269
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Nguy\xe1\xbb\x85n Ho\xc3\xa0ng Th\xe1\xba\xa1ch of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-529/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the UrbBuf_getDataBuf function. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280

## Disclosure Timeline

- 2024-04-29 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
