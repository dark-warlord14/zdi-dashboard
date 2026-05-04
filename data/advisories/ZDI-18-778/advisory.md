# ZDI-18-778: Hewlett Packard Enterprise Intelligent Management Center tftpserver getFileData Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-778
- **ZDI-CAN:** ZDI-CAN-5749
- **Date:** 2018-07-26
- **CVE:** CVE-2018-7074
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-778/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the m_pkg_LimitSize parameter provided to the tftpserver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=hpesbhf03864en_us

## Disclosure Timeline

- 2018-03-08 - Vulnerability reported to vendor
- 2018-07-26 - Coordinated public release of advisory
- 2018-07-26 - Advisory Updated
