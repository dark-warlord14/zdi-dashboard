# ZDI-18-879: (Pwn2Own) Huawei App Market Whitelist Bypass Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-879
- **ZDI-CAN:** ZDI-CAN-5347
- **Date:** 2018-08-02
- **CVE:** CVE-2018-7931
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Huawei
- **Affected Products:** App Market
- **Credit:** MWR Labs - Alex Plaskett James Loureiro Robert Miller and Georgi Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-879/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Huawei App Market. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of whitelisted domains. The issue lies in the lack of verification that content was loaded over a secure channel. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the application.

## Additional Details

Huawei has issued an update to correct this vulnerability. More details can be found at: https://www.huawei.com/en/psirt/security-advisories/huawei-sa-20180423-01-app-en

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-08-02 - Coordinated public release of advisory
- 2018-08-02 - Advisory Updated
