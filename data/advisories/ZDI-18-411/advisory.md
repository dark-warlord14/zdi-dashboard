# ZDI-18-411: Trend Micro Encryption for Email Gateway DBCrypto Authentication Weakness Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-411
- **ZDI-CAN:** ZDI-CAN-5513
- **Date:** 2018-05-04
- **CVE:** CVE-2018-10355
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Encryption for Email Gateway
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-411/
## Vulnerability Details

This vulnerability allows attackers to recover user passwords on vulnerable installations of Trend Micro Encryption for Email Gateway. An attacker must first obtain access to the user database on the target system in order to exploit this vulnerability. The specific flaw exists within the DBCrypto class. When storing user passwords, the process stores them in a recoverable format using a hard-coded key. An attacker can then leverage this vulnerability to decrypt existing passwords.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119349

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
