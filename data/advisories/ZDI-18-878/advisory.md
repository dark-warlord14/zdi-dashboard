# ZDI-18-878: (Pwn2Own) Huawei Reader FileName Directory Traversal Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-878
- **ZDI-CAN:** ZDI-CAN-5349
- **Date:** 2018-08-02
- **CVE:** CVE-2017-15309
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Huawei
- **Affected Products:** Reader
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-878/
## Vulnerability Details

This vulnerability allows local attackers to create arbitrary files on vulnerable installations of Huawei Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of FileName parameters. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Huawei has issued an update to correct this vulnerability. More details can be found at: http://www.huawei.com/en/psirt/security-advisories/2017/huawei-sa-20171120-01-hwreader-en

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
