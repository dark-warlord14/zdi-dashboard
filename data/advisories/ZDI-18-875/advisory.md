# ZDI-18-875: (Pwn2Own) Huawei App Market JavaScript Bridge Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-875
- **ZDI-CAN:** ZDI-CAN-5348
- **Date:** 2018-08-02
- **CVE:** CVE-2018-7932
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Huawei
- **Affected Products:** App Market
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-875/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Huawei App Market. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the launchApp method within the HiSpaceObject JavaScript interface. The issue lies in the lack of verification of the user-supplied arguments. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Huawei has issued an update to correct this vulnerability. More details can be found at: https://www.huawei.com/en/psirt/security-advisories/huawei-sa-20180423-01-app-en

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
