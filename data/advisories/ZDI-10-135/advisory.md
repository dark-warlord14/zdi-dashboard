# ZDI-10-135: Novell Groupwise WebAccess Multiple Cross-Site Scripting Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-135
- **ZDI-CAN:** ZDI-CAN-710
- **Date:** 2010-07-20
- **CVE:** CVE-2010-2778 , CVE-2010-2779
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** GroupWise WebAccess
- **Credit:** scriptjunkie scriptjunkie1 {nospam} googlemail {nospam} com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary client side script on vulnerable installations of Novell Groupwise WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling html messages sent to a Novell Groupwise WebAccess user. Messages are improperly sanitized allowing client side script to be supplied to the user's web browser resulting in the user's WebAccess credentials being compromised.

## Additional Details

http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7006375&sliceId=2&docTypeID=DT_TID_1_1&dialogID=155271273&stateId=0%200%20155267615 http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7006376&sliceId=2&docTypeID=DT_TID_1_1&dialogID=155271386&stateId=0%200%20155267712

## Disclosure Timeline

- 2010-04-05 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
