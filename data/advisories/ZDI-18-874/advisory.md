# ZDI-18-874: (Pwn2Own) Huawei Reader onChapPack Directory Traversal File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-874
- **ZDI-CAN:** ZDI-CAN-5350
- **Date:** 2018-08-02
- **CVE:** CVE-2017-15309
- **CVSS:** 3.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:N/I:P/A:P
- **Affected Vendors:** Huawei
- **Affected Products:** Reader
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-874/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on vulnerable installations of Huawei Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the onChapPack function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any files accessible to the user.

## Additional Details

Huawei has issued an update to correct this vulnerability. More details can be found at: http://www.huawei.com/en/psirt/security-advisories/2017/huawei-sa-20171120-01-hwreader-en

## Disclosure Timeline

- 2017-11-02 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
