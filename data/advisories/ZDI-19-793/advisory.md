# ZDI-19-793: Red Lion Crimson CD31 File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-793
- **ZDI-CAN:** ZDI-CAN-8301
- **Date:** 2019-09-05
- **CVE:** CVE-2019-10978
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Red Lion
- **Affected Products:** Crimson
- **Credit:** Michael DePlante, Anthony Fuller and Todd Manning of Trend Micro Zero Day Initiative/Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-793/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Red Lion Crimson. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CD31 files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Red Lion has issued an update to correct this vulnerability. More details can be found at: https://support.redlion.net/hc/en-us/articles/360033077531

## Disclosure Timeline

- 2019-04-26 - Vulnerability reported to vendor
- 2019-09-05 - Coordinated public release of advisory
