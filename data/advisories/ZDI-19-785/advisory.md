# ZDI-19-785: Red Lion Crimson Hard-coded Cryptographic Key Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-785
- **ZDI-CAN:** ZDI-CAN-8188
- **Date:** 2019-09-05
- **CVE:** CVE-2019-10990
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Red Lion
- **Affected Products:** Crimson
- **Credit:** Michael DePlante, Anthony Fuller and Todd Manning of Trend Micro Zero Day Initiative/Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-785/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Red Lion Crimson. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CTextStreamMemory class. The class contains hard-coded secrets in clear text. An attacker can leverage this to decrypt user passwords.

## Additional Details

Red Lion has issued an update to correct this vulnerability. More details can be found at: https://support.redlion.net/hc/en-us/articles/360033077531

## Disclosure Timeline

- 2019-02-28 - Vulnerability reported to vendor
- 2019-09-05 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
