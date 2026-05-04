# ZDI-13-241: Hewlett-Packard Intelligent Management Center CommonUtils Static DES/ECB Decryption Key Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-241
- **ZDI-CAN:** ZDI-CAN-1645
- **Date:** 2013-10-16
- **CVE:** CVE-2013-4825
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-241/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CommonUtil class. This application uses a static key and the DES algorithm in ECB mode to store Administrator credentials. A remote attacker can use this vulnerability in conjunction with other vulnerabilities to disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03943547

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
