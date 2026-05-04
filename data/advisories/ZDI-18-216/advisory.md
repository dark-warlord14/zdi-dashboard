# ZDI-18-216: Trend Micro Maximum Security Regex Matching Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-216
- **ZDI-CAN:** ZDI-CAN-4911
- **Date:** 2018-02-27
- **CVE:** CVE-2016-1699
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-216/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Maximum Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the analysis of web pages. By performing actions in script matching a large array against a RegEx, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1119392.aspx

## Disclosure Timeline

- 2017-10-20 - Vulnerability reported to vendor
- 2018-02-27 - Coordinated public release of advisory
- 2018-02-27 - Advisory Updated
