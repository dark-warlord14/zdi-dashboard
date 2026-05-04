# ZDI-06-024: eIQnetworks Enterprise Security Analyzer License Manager Buffer Overflow

## Metadata

- **ZDI ID:** ZDI-06-024
- **ZDI-CAN:** ZDI-CAN-052
- **Date:** 2006-07-25
- **CVE:** CVE-2006-3838
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** eIQnetworks
- **Affected Products:** Enterprise Security Analyzer
- **Credit:** Titon, JxT, KF and the rest of Bastard Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of eIQnetworks Enterprise Security Analyzer. Authentication is not required to exploit this vulnerability. The specific flaw exists within EnterpriseSecurityAnalyzer.exe, which binds by default to TCP port 10616. During the processing of long arguments to the LICMGR_ADDLICENSE command a classic stack based buffer overflow occurs.

## Additional Details

eIQnetworks has issued an update to correct this vulnerability. More details can be found at: http://www.eiqnetworks.com/products/enterprisesecurity/EnterpriseSecurityAnalyzer/ESA_2.5.0_Release_Notes.pdf

## Disclosure Timeline

- 2006-05-10 - Vulnerability reported to vendor
- 2006-07-25 - Coordinated public release of advisory
