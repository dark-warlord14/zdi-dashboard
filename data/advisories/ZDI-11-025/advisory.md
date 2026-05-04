# ZDI-11-025: Novell GroupWise Internet Agent REQUEST-STATUS Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-025
- **ZDI-CAN:** ZDI-CAN-955
- **Date:** 2011-01-25
- **CVE:** CVE-2010-4326
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell GroupWise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gwwww1.dll module responsible for parsing VCALENDAR data within e-mail messages. When the code encounters a REQUEST-STATUS variable it allocates up to 0xFFFF bytes for the variable's value. It then proceeds to copy the value into the fixed-length buffer without checking if it will fit. By specifying a large enough string in the e-mail, an attacker can overflow the buffer and execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7007155&sliceId=1&docTypeID=DT_TID_1_1&dialogID=199990003&stateId=0%200%20199988016

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2011-01-25 - Coordinated public release of advisory
